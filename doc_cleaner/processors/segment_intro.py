"""
段落摘要处理器 - 使用 LLM 生成文档和章节的摘要信息

利用大语言模型（LLM）自动生成：
- 文档概要（概览文档的核心内容）
- 各章节摘要（概括每段的要点）
- 逻辑关系分析（章节间的深层关联）

处理器会清理旧的上下文块，并重新生成。
"""

import re
import json
from ..utils.config import get_config
from ..utils.llm_client import LLMClient
from ..utils.logger import get_logger
from typing import List, Dict, Optional, Tuple


class SegmentIntroProcessor:
    """
    为文档段落生成摘要和上下文说明

    使用 LLM 分析文档结构，生成文档级摘要和章节级摘要，
    并将分析结果嵌入 Markdown 文档中。
    """

    def __init__(self):
        # 延迟初始化 LLM 客户端，实际使用时才创建
        self._llm_client = None

    @property
    def llm_client(self) -> LLMClient:
        """获取或创建 LLM 客户端实例（延迟初始化模式）"""
        if self._llm_client is None:
            config = get_config()
            self._llm_client = LLMClient(
                api_key=config['llm']['api_key'],
                base_url=config['llm']['base_url'],
                model=config['llm']['model'],
                timeout=config['llm'].get('timeout', 120),
                max_tokens=config['llm'].get('max_tokens', 8192),
            )
        return self._llm_client

    def process(self, content: str) -> str:
        """
        为文档段落添加摘要和上下文

        需求7：阅读完整文件内容，提炼200字符内的文档概要，
               在每个大的段落（一级/二级标题）开头添加文档概要和当前段落说明
        需求8：在每个大的段落开头添加关联关系说明
        """
        content = self._clean_old_context_blocks(content)

        sections = self._extract_sections(content)

        if not sections:
            return content

        content = self._clean_old_intro(content)

        document_summary = self._generate_document_summary(content)

        section_summaries = self._generate_section_summaries(content, sections)

        logical_relations = self._analyze_logical_relations(content, sections)

        structural_relations = self._build_section_relationships(sections)

        result = self._embed_context_blocks(
            content, document_summary, section_summaries,
            sections, logical_relations, structural_relations
        )

        return result

    def _clean_old_context_blocks(self, content: str) -> str:
        """移除已有的旧上下文块和旧摘要信息"""
        lines = content.split('\n')
        filtered_lines = []
        skip_block = False
        context_start_markers = (
            '**文档上下文**', '**文档概要**', '**本段概要**', '**逻辑关联**',
            '文档概要：', '本段概要：', '逻辑关联：', '逻辑关联分析：', '本章概要：',
        )

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped == '---':
                if skip_block:
                    # 上下文块结束标记，跳过此行并结束跳过模式
                    skip_block = False
                    continue
                # 检查 --- 后面是否紧跟上下文块内容
                is_boundary = False
                # 向后查找：--- 后面的非空行是否为上下文标记
                for j in range(i + 1, min(i + 5, len(lines))):
                    next_stripped = lines[j].strip()
                    if next_stripped:
                        if any(next_stripped.startswith(m) for m in context_start_markers):
                            is_boundary = True
                        break
                # 向前查找：filtered_lines 中最近的非空行是否为上下文标记
                if not is_boundary:
                    for j in range(len(filtered_lines) - 1, -1, -1):
                        prev_stripped = filtered_lines[j].strip()
                        if prev_stripped:
                            if any(prev_stripped.startswith(m) for m in context_start_markers):
                                is_boundary = True
                            break

                if is_boundary:
                    skip_block = True
                    # 移除前面的上下文标记行和空行
                    while filtered_lines and (not filtered_lines[-1].strip() or
                           filtered_lines[-1].strip() in context_start_markers):
                        filtered_lines.pop()
                    continue

            if skip_block:
                continue

            # 跳过独立的上下文标记行（不在 --- 块内的残留行）
            if any(stripped.startswith(m) for m in context_start_markers):
                continue
            # 跳过旧的结构关系标记行
            if stripped.startswith(('当前位置：', '所属章节：', '上一节：', '下一节：',
                                     '包含小节：', '上一章：', '下一章：')):
                continue

            filtered_lines.append(line)

        return '\n'.join(filtered_lines)

    def _extract_sections(self, content: str) -> List[Dict]:
        """从文档中提取所有章节标题及其级别，支持 Markdown 标题和数字编号段落"""
        sections = []
        lines = content.split('\n')
        in_code_block = False

        toc_map = self._extract_toc_titles(lines)

        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('```'):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            if re.match(r'^#{1,6}\s', stripped):
                level = len(stripped) - len(stripped.lstrip('#'))
                title = stripped.lstrip('#').strip()
                # 剥离标题尾部的闭合 #（如 "# 标题 #" -> "标题"）
                title = title.rstrip('#').strip()
                sections.append({
                    'level': level,
                    'title': title,
                    'line': i,
                    'content': ''
                })
            elif self._is_numbered_heading(stripped):
                result = self._parse_numbered_heading(stripped)
                if result:
                    level, number, title = result
                    if number in toc_map:
                        title = toc_map[number]
                    sections.append({
                        'level': level,
                        'title': title,
                        'number': number,
                        'line': i,
                        'content': ''
                    })

        logger = get_logger()
        if sections:
            md_count = sum(1 for s in sections if 'number' not in s)
            num_count = sum(1 for s in sections if 'number' in s)
            logger.info(
                f"章节识别完成：共 {len(sections)} 个章节"
                f"（Markdown 标题 {md_count}，数字编号 {num_count}）"
            )
        else:
            logger.info("未识别到任何章节标题")

        return sections

    @staticmethod
    def _extract_toc_titles(lines: List[str]) -> Dict[str, str]:
        """从目录页中提取章节编号到标题的映射"""
        toc_map = {}
        toc_pattern = re.compile(
            r'^(\d+(?:\.\d+)*)\s+(.+?)\s*[.…]{3,}\s*\d+\s*$'
        )
        for line in lines[:50]:
            stripped = line.strip()
            match = toc_pattern.match(stripped)
            if match:
                number = match.group(1)
                title = match.group(2).strip()
                title = re.sub(r'\s+', ' ', title)
                if title:
                    toc_map[number] = title
        return toc_map

    @staticmethod
    def _is_numbered_heading(text: str) -> bool:
        """判断文本是否为数字编号章节标题，排除目录条目"""
        if not text:
            return False
        if re.search(r'\.{4,}', text) or re.search(r'…{2,}', text):
            return False
        match = re.match(r'^(\d+(?:\.\d+)*)\s+(.+)', text)
        if not match:
            return False
        number = match.group(1)
        title_part = match.group(2).strip()
        dot_count = number.count('.')
        if dot_count > 5:
            return False
        first_words = re.split(r'[\s,，。；：]', title_part)[:6]
        first_text = ''.join(first_words)
        if len(first_text) < 2:
            return False
        return True

    @staticmethod
    def _parse_numbered_heading(text: str) -> Optional[Tuple[int, str, str]]:
        """解析数字编号章节标题，返回 (层级, 编号, 标题)"""
        match = re.match(r'^(\d+(?:\.\d+)*)\s+(.+)', text)
        if not match:
            return None
        number = match.group(1)
        title = match.group(2).strip()
        title = re.sub(r'[.…]{3,}\s*\d+$', '', title).strip()
        title = re.sub(r'\s+', ' ', title).strip()
        level = number.count('.') + 1
        return level, number, title

    def _clean_old_intro(self, content: str) -> str:
        """清理文档中残留的旧摘要信息"""
        lines = content.split('\n')
        result = []

        for line in lines:
            stripped = line.strip()
            # 跳过旧的摘要头部
            if (stripped.startswith('文档概要：') or
                stripped.startswith('本章概要：') or
                stripped.startswith('逻辑关联分析：')):
                continue
            result.append(line)

        return '\n'.join(result)

    def _generate_document_summary(self, content: str) -> str:
        """
        使用 LLM 生成文档概要

        向 LLM 发送文档头部内容（前 3000 字符），
        请求生成简洁的文档概要。
        """
        logger = get_logger()
        try:
            summary = self.llm_client.summarize_document(content)
            if summary:
                summary = self._strip_prefix(summary, '文档概要：')
            return summary or ""
        except Exception as e:
            logger.error(f"生成文档概要失败：{e}")
            return ""

    def _generate_section_summaries(self, content: str, sections: List[Dict]) -> Dict[str, str]:
        """
        使用 LLM 生成各章节的摘要

        将所有章节标题合并为一次 LLM 调用，减少 API 请求次数。
        仅为大段落（一级/二级标题）生成摘要，跳过子段落。
        """
        logger = get_logger()
        summaries = {}
        major_levels = self._get_major_levels(sections)
        major_sections = [s for s in sections if s['level'] in major_levels]

        if not major_sections:
            return summaries

        try:
            summary = self.llm_client.summarize_sections_batch(major_sections, content)
            if summary:
                parsed = self._parse_batch_summaries(summary, major_sections)
                # 硬性截断：确保每个章节摘要不超过 50 字符
                for title in parsed:
                    if len(parsed[title]) > 50:
                        parsed[title] = parsed[title][:47] + '...'
                summaries.update(parsed)
        except Exception as e:
            logger.warning(f"批量生成章节摘要失败，回退到逐个生成：{e}")
            for idx, section in enumerate(major_sections):
                try:
                    original_idx = sections.index(section)
                    section_content = self._get_section_content(content, sections, original_idx)
                    summary = self.llm_client.summarize_section(section['title'], section_content)
                    if summary:
                        summary = self._strip_prefix(summary, '本章概要：')
                        summaries[section['title']] = summary
                except Exception as e2:
                    logger.warning(f"生成章节 '{section['title']}' 摘要失败：{e2}")
                    continue

        return summaries

    def _parse_batch_summaries(self, text: str, sections: List[Dict]) -> Dict[str, str]:
        """
        解析批量摘要 LLM 返回的文本

        按章节标题拆分，提取每个章节的摘要。
        """
        result = {}
        if not text or not sections:
            return result

        lines = text.split('\n')
        current_section = None
        current_lines = []

        for line in lines:
            matched = False
            for s in sections:
                if s['title'] in line:
                    if current_section and current_lines:
                        result[current_section] = '\n'.join(current_lines).strip()
                    current_section = s['title']
                    remainder = line.replace(s['title'], '').strip().lstrip('：:-').strip()
                    current_lines = [remainder] if remainder else []
                    matched = True
                    break
            if not matched and current_section:
                current_lines.append(line)

        if current_section and current_lines:
            result[current_section] = '\n'.join(current_lines).strip()

        return result

    def _get_section_content(self, content: str, sections: List[Dict], idx: int) -> str:
        """提取指定章节的内容文本"""
        lines = content.split('\n')

        # 章节起始行
        start_line = sections[idx]['line']

        # 章节结束行（下一个同级或更高级别章节的前一行）
        if idx < len(sections) - 1:
            end_line = sections[idx + 1]['line'] - 1
        else:
            end_line = len(lines) - 1

        # 取前 1000 字符作为章节内容的代表
        section_lines = lines[start_line:end_line + 1]
        section_text = '\n'.join(section_lines)
        return section_text[:1000]

    def _analyze_logical_relations(self, content: str, sections: List[Dict]) -> Dict[str, str]:
        """
        使用 LLM 分析文档章节间的逻辑关系

        返回每个章节的关联关系描述，而非全局分析文本。
        """
        logger = get_logger()
        try:
            section_titles = [s['title'] for s in sections]
            relations = self.llm_client.analyze_logical_relations(section_titles)
            if relations:
                relations = self._strip_prefix(relations, '逻辑关联分析：')
            return self._parse_logical_relations(relations or "", sections)
        except Exception as e:
            logger.error(f"分析逻辑关联失败：{e}")
            return {}

    def _parse_logical_relations(self, relations_text: str, sections: List[Dict]) -> Dict[str, str]:
        """
        将 LLM 返回的逻辑关联文本解析为每个章节的关联描述

        尝试按章节标题拆分 LLM 返回的文本，
        为每个大段落提取与自身相关的逻辑关联描述。
        """
        if not relations_text or not sections:
            return {}

        major_levels = self._get_major_levels(sections)
        major_sections = [s for s in sections if s['level'] in major_levels]
        if not major_sections:
            return {}

        result = {}

        lines = relations_text.split('\n')
        current_section = None
        current_lines = []

        for line in lines:
            matched = False
            for s in major_sections:
                if s['title'] in line:
                    if current_section and current_lines:
                        result[current_section] = '\n'.join(current_lines).strip()
                    current_section = s['title']
                    remainder = line.replace(s['title'], '').strip().lstrip('：:-').strip()
                    current_lines = [remainder] if remainder else []
                    matched = True
                    break
            if not matched:
                current_lines.append(line)

        if current_section and current_lines:
            result[current_section] = '\n'.join(current_lines).strip()

        return result

    def _build_section_relationships(self, sections: List[Dict]) -> Dict[str, str]:
        """
        基于文档结构自动构建章节间的关联关系描述

        识别的关系类型：
        - 父章节（所属章节）
        - 前驱/后继章节
        - 子章节列表
        """
        relationships = {}
        major_levels = self._get_major_levels(sections)

        for i, section in enumerate(sections):
            if section['level'] not in major_levels:
                continue

            parts = []

            for j in range(i - 1, -1, -1):
                if sections[j]['level'] < section['level']:
                    parts.append(f"所属章节：{sections[j]['title']}")
                    break

            for j in range(i + 1, len(sections)):
                if sections[j]['level'] > section['level']:
                    parts.append(f"包含小节：{sections[j]['title']}")
                    break

            prev_major = None
            for j in range(i - 1, -1, -1):
                if sections[j]['level'] <= section['level']:
                    prev_major = sections[j]['title']
                    break
            if prev_major:
                parts.append(f"上一节：{prev_major}")

            next_major = None
            for j in range(i + 1, len(sections)):
                if sections[j]['level'] <= section['level']:
                    next_major = sections[j]['title']
                    break
            if next_major:
                parts.append(f"下一节：{next_major}")

            if parts:
                relationships[section['title']] = '\n'.join(parts)

        return relationships

    @staticmethod
    def _strip_prefix(text: str, prefix: str) -> str:
        """移除 LLM 返回文本中的指定前缀（兼容全角/半角冒号）"""
        if text.startswith(prefix):
            return text[len(prefix):].strip()
        half_width = prefix.replace('：', ':')
        if text.startswith(half_width):
            return text[len(half_width):].strip()
        return text

    def _embed_context_blocks(self, content: str, document_summary: str,
                               section_summaries: Dict[str, str],
                               sections: List[Dict],
                               logical_relations: Dict[str, str],
                               structural_relations: Dict[str, str]) -> str:
        """
        将文档概要、段落说明和逻辑关联嵌入文档中

        需求7：在每个大段落（文档中最高层级标题）开头添加文档概要 + 当前段落说明
        需求8：在每个大段落开头添加关联关系说明
        """
        lines = content.split('\n')
        result_lines = []
        in_code_block = False

        major_levels = self._get_major_levels(sections)

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped.startswith('```'):
                in_code_block = not in_code_block
                result_lines.append(line)
                continue

            if in_code_block:
                result_lines.append(line)
                continue

            current_title = None
            current_level = None

            if re.match(r'^#{1,6}\s', stripped):
                current_level = len(stripped) - len(stripped.lstrip('#'))
                current_title = stripped.lstrip('#').strip()
                # 剥离标题尾部的闭合 #（如 "# 标题 #" -> "标题"）
                current_title = current_title.rstrip('#').strip()
            else:
                for section in sections:
                    if section['line'] == i and 'number' in section:
                        current_level = section['level']
                        current_title = section['title']
                        break

            result_lines.append(line)

            if current_title and current_level and current_level in major_levels:
                context_lines = []

                if document_summary:
                    context_lines.append(f"文档概要：{document_summary}")

                if current_title in section_summaries and section_summaries[current_title]:
                    context_lines.append(f"本段概要：{section_summaries[current_title]}")

                relation_parts = []
                if current_title in structural_relations and structural_relations[current_title]:
                    relation_parts.append(structural_relations[current_title])
                if current_title in logical_relations and logical_relations[current_title]:
                    relation_parts.append(logical_relations[current_title])

                if relation_parts:
                    context_lines.append("逻辑关联：" + "；".join(relation_parts))

                if context_lines:
                    result_lines.append('')
                    result_lines.append('---')
                    for cl in context_lines:
                        result_lines.append(cl)
                    result_lines.append('---')

        return '\n'.join(result_lines)

    @staticmethod
    def _get_major_levels(sections: List[Dict]) -> set:
        """
        判断文档中的"大段落"标题层级

        规则：取文档中实际出现的最高层级标题和次高层级标题作为大段落。
        例如，如果文档只有 ### 标题，则 ### 就是大段落。
        如果文档有 ## 和 ### 标题，则 ## 是大段落。
        """
        if not sections:
            return set()

        levels = sorted(set(s['level'] for s in sections))
        major = set()
        if levels:
            major.add(levels[0])
        if len(levels) > 1:
            major.add(levels[1])
        return major
