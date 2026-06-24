"""
格式标准化处理器 - 确保 Markdown 格式规范

处理内容包括：
- 标题格式标准化（# 后确保一个空格）
- 列表格式标准化（统一的标记符号和缩进）
- 代码块前后空行
- 水平线标准化
- 标题前后空行
- 表格格式标准化
- 移除行尾多余空格
"""

import re


class FormatStandardizationProcessor:
    """确保 Markdown 文件遵循标准格式规范"""

    def process(self, content: str) -> str:
        """应用格式标准化操作"""
        result = content

        # 统一标题格式："# 标题"（# 后确保一个空格）
        result = self._standardize_headings(result)

        # 统一列表格式
        result = self._standardize_lists(result)

        # 确保代码块前后有空行
        result = self._standardize_code_blocks(result)

        # 统一水平线为 ---
        result = self._standardize_horizontal_rules(result)

        # 移除行尾多余空格
        result = self._remove_trailing_spaces(result)

        # 确保标题后有空行
        result = self._ensure_blank_after_headings(result)

        # 标准化表格格式
        result = self._standardize_tables(result)

        # 确保标题前有空行
        result = self._ensure_blank_before_headings(result)

        return result

    def _standardize_headings(self, text: str) -> str:
        """确保标题格式统一：# 后有一个空格，并剥离尾部闭合 #"""
        lines = text.split('\n')
        result = []

        for line in lines:
            stripped = line.strip()
            if stripped.startswith('#'):
                hash_count = len(stripped) - len(stripped.lstrip('#'))
                heading_text = stripped[hash_count:].strip()
                # 剥离标题尾部的闭合 #（如 "# 标题 #" -> "标题"）
                heading_text = heading_text.rstrip('#').strip()
                if heading_text:
                    standardized = '#' * hash_count + ' ' + heading_text
                    result.append(standardized)
                else:
                    result.append(line)
            else:
                result.append(line)

        return '\n'.join(result)

    def _standardize_lists(self, text: str) -> str:
        """统一列表项格式：标准化标记符号和缩进"""
        lines = text.split('\n')
        result = []

        for i, line in enumerate(lines):
            stripped = line.lstrip()
            indent = len(line) - len(stripped)

            # 处理无序列表：保留最多 3 个空格缩进，去除多余空格
            if stripped.startswith(('- ', '* ', '+ ')):
                marker_end = 2
                content = stripped[marker_end:]
                result.append(' ' * min(indent, 3) + stripped[:marker_end] + content.lstrip())
            # 处理有序列表：标准化 "数字. " 格式
            elif re.match(r'^\d+\.\s', stripped):
                match = re.match(r'^(\s*)(\d+\.\s)(.*)$', line)
                if match:
                    indent_str, marker, content = match.groups()
                    result.append(indent_str + marker + content.lstrip())
                else:
                    result.append(line)
            else:
                result.append(line)

        return '\n'.join(result)

    def _standardize_code_blocks(self, text: str) -> str:
        """确保代码块前后有空行"""
        lines = text.split('\n')
        result = []
        in_code_block = False

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped.startswith('```'):
                if not in_code_block:
                    # 代码块开始前插入空行
                    if result and result[-1].strip():
                        result.append('')
                in_code_block = not in_code_block
                result.append(line)
                if not in_code_block:
                    # 代码块结束后插入空行
                    if i < len(lines) - 1 and lines[i + 1].strip():
                        result.append('')
            else:
                result.append(line)

        return '\n'.join(result)

    def _standardize_horizontal_rules(self, text: str) -> str:
        """
        统一水平线为 ---，并确保前后有空行

        跳过文档上下文块中的 --- 边界标记，避免破坏其结构。
        上下文块特征：--- 紧跟在标题行后，且后续行包含上下文标记字段。
        """
        lines = text.split('\n')
        result = []
        hr_patterns = ['---', '***', '___']

        # 上下文块标记字段前缀
        context_markers = (
            '文档概要：', '本段概要：', '逻辑关联：',
            '**文档上下文**', '**文档概要**', '**本段概要**', '**逻辑关联**',
        )

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped in hr_patterns:
                # 检查是否为文档上下文块的边界标记
                is_context_boundary = False

                # 向后检查：--- 后面的非空行是否为上下文标记
                for j in range(i + 1, min(i + 4, len(lines))):
                    next_stripped = lines[j].strip()
                    if next_stripped:
                        if any(next_stripped.startswith(m) for m in context_markers):
                            is_context_boundary = True
                        break

                # 向前检查：--- 前面的非空行是否为上下文标记
                if not is_context_boundary:
                    for j in range(i - 1, max(i - 4, -1), -1):
                        prev_stripped = lines[j].strip()
                        if prev_stripped:
                            if any(prev_stripped.startswith(m) for m in context_markers):
                                is_context_boundary = True
                            break

                if is_context_boundary:
                    result.append(stripped)
                    continue

                # 标准化水平线，确保前后有空行
                if result and result[-1].strip():
                    result.append('')
                result.append(stripped)
                if i < len(lines) - 1 and lines[i + 1].strip():
                    result.append('')
            else:
                result.append(line)

        return '\n'.join(result)

    def _remove_trailing_spaces(self, text: str) -> str:
        """移除所有行尾的空白字符"""
        lines = text.split('\n')
        result = [line.rstrip() for line in lines]
        return '\n'.join(result)

    def _ensure_blank_after_headings(self, text: str) -> str:
        """确保每个标题后面都有空行"""
        lines = text.split('\n')
        result = []

        for i, line in enumerate(lines):
            result.append(line)
            stripped = line.strip()
            if stripped.startswith('#') and i < len(lines) - 1:
                next_line = lines[i + 1]
                if next_line.strip():
                    result.append('')

        return '\n'.join(result)

    def _ensure_blank_before_headings(self, text: str) -> str:
        """确保每个标题前面都有空行（文档第一个标题除外）"""
        lines = text.split('\n')
        result = []

        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('#') and result:
                if result[-1].strip():
                    result.append('')
            result.append(line)

        return '\n'.join(result)

    def _standardize_tables(self, text: str) -> str:
        """补充表格格式标准化（与 TableProcessor 配合使用）"""
        lines = text.split('\n')
        result = []

        i = 0
        while i < len(lines):
            line = lines[i]
            if line.strip().startswith('|') and self._is_table_line(line):
                # 收集连续的表格行
                table_lines = []
                while i < len(lines) and (lines[i].strip().startswith('|') or lines[i].strip() == ''):
                    if lines[i].strip().startswith('|'):
                        table_lines.append(lines[i])
                    i += 1

                if table_lines:
                    result.extend(table_lines)
                    # 表格后插入空行
                    if i < len(lines) and lines[i].strip():
                        result.append('')
                continue
            else:
                result.append(line)
                i += 1

        return '\n'.join(result)

    def _is_table_line(self, line: str) -> bool:
        """检查行是否为 Markdown 表格的一部分"""
        stripped = line.strip()
        if re.match(r'^\|[\s:-]+\|[\s:-]+(?:\|[\s:-]+)*\|?$', stripped):
            return True
        # 必须以 | 开头或结尾，且包含至少 2 个 |
        if stripped.count('|') >= 2 and (stripped.startswith('|') or stripped.endswith('|')):
            return True
        return False
