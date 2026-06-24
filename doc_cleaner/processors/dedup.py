"""
去重处理器 - 移除文档中的重复内容

使用 MD5 哈希对段落进行精确去重，
保留首次出现的段落，删除后续重复段落。
"""

import hashlib
import re


class DedupProcessor:
    """删除重复段落，保留首次出现的唯一内容"""

    def process(self, content: str) -> str:
        """应用去重操作"""
        # 保护代码块，避免代码块内的重复内容被误删
        code_blocks = []
        placeholder_pattern = '__DEDUP_CODE_c4f7_{}__'

        def save_code_block(match):
            idx = len(code_blocks)
            code_blocks.append(match.group(0))
            return placeholder_pattern.format(idx)

        # 提取并替换代码块为占位符
        result = re.sub(r'```[\s\S]*?```', save_code_block, content)

        # 按空行分割为段落
        paragraphs = self._split_paragraphs(result)

        # 移除重复段落（精确匹配）
        unique_paragraphs = self._remove_duplicate_paragraphs(paragraphs)

        # 用双换行重新组合
        result = '\n\n'.join(unique_paragraphs)

        # 恢复代码块
        for idx, block in enumerate(code_blocks):
            result = result.replace(placeholder_pattern.format(idx), block)

        return result

    def _split_paragraphs(self, text: str) -> list:
        """将文本按空行分割为段落列表"""
        raw_paragraphs = text.split('\n\n')
        paragraphs = [p.strip() for p in raw_paragraphs if p.strip()]
        return paragraphs

    def _remove_duplicate_paragraphs(self, paragraphs: list) -> list:
        """
        移除重复段落，保持原始顺序

        使用 MD5 哈希值作为唯一性判断依据，
        只有内容完全相同的段落才会被判定为重复
        """
        seen = set()
        unique = []

        for para in paragraphs:
            para_hash = hashlib.md5(para.encode('utf-8')).hexdigest()
            if para_hash not in seen:
                seen.add(para_hash)
                unique.append(para)

        return unique
