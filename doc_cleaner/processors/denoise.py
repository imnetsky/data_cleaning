"""
去噪处理器 - 移除文档中的无关内容和噪声

处理内容包括：
- 页眉和页脚（重复出现的行模式）
- 页面编号
- 多余空白和制表符
- 行尾空格
- 过多的空行
- 代码块保护（避免误处理代码内容）
"""

import re
from collections import Counter


class DenoiseProcessor:
    """移除页眉、页脚、页码、空行、多余空格和制表符"""

    def process(self, content: str) -> str:
        """应用去噪操作"""
        result = content

        # 保护代码块，避免空格/制表符转换破坏代码格式
        code_blocks = []
        def save_code_block(match):
            idx = len(code_blocks)
            code_blocks.append(match.group(0))
            return f'__DENOISE_CODE_b2e1_{idx}__'
        result = re.sub(r'```[\s\S]*?```', save_code_block, result)

        # 将制表符替换为 4 个空格
        result = result.replace('\t', '    ')

        # 将 3 个以上连续空格缩减为 1 个
        result = re.sub(r' {3,}', ' ', result)

        # 移除每行行尾的空白字符
        result = self._trim_lines(result)

        # 移除页码和页脚模式
        result = self._remove_page_numbers(result)

        # 移除重复出现的页眉页脚行
        result = self._remove_repeated_headers_footers(result)

        # 将 3 行以上的连续空行缩减为 2 行
        result = self._remove_excess_blank_lines(result)

        # 恢复代码块
        for idx, block in enumerate(code_blocks):
            result = result.replace(f'__DENOISE_CODE_b2e1_{idx}__', block)

        return result

    def _remove_excess_blank_lines(self, text: str) -> str:
        """将 3 行及以上的连续空行缩减为 2 行"""
        return re.sub(r'\n{3,}', '\n\n', text)

    def _trim_lines(self, text: str) -> str:
        """移除每行行尾的空白字符"""
        lines = text.split('\n')
        trimmed = [line.rstrip() for line in lines]
        return '\n'.join(trimmed)

    def _remove_page_numbers(self, text: str) -> str:
        """移除常见的页码和页脚模式"""
        lines = text.split('\n')
        filtered = []

        # 匹配常见页码格式的正则表达式列表
        page_patterns = [
            r'^Page\s*\d+$',          # "Page 1", "Page 123"
            r'^-\s*\d+\s*-$',          # "- 1 -"
            r'^\[\s*\d+\s*\]$',        # "[1]"
            r'^\s*\d+\s*/\s*\d+\s*$',  # "1/10"
            r'^第\s*\d+\s*页$',         # "第 1 页"
            r'^-\s*第\s*\d+\s*页\s*-$', # "- 第 1 页 -"
        ]

        for line in lines:
            stripped = line.strip()
            is_page_number = False
            # 检查是否匹配页码模式
            for pattern in page_patterns:
                if re.match(pattern, stripped, re.IGNORECASE):
                    is_page_number = True
                    break
            # 独立数字且长度 ≤4，且前一行为空行或不存在，则视为页码
            if stripped.isdigit() and len(stripped) <= 4:
                if not filtered or not filtered[-1].strip():
                    is_page_number = True
            if not is_page_number:
                filtered.append(line)

        return '\n'.join(filtered)

    def _remove_repeated_headers_footers(self, text: str) -> str:
        """
        移除重复出现的页眉页脚行

        检测逻辑：在非空行中，如果某行文本重复出现 3 次及以上，
        且该行较短（≤80字符）、非 Markdown 标题/列表/表格/代码块元素，
        则视为页眉或页脚并移除。
        """
        lines = text.split('\n')
        non_blank_lines = [line.strip() for line in lines if line.strip()]

        if not non_blank_lines:
            return text

        # 统计非空行出现频率
        line_counts = Counter(non_blank_lines)
        total_lines = len(non_blank_lines)

        # 识别页眉页脚候选行：重复出现 3 次及以上，且占比合理
        header_footer_lines = set()
        for line_text, count in line_counts.items():
            if count >= 3 and len(line_text) <= 80:
                # 排除 Markdown 块级元素，避免误删标题、列表等
                if self._is_likely_header_footer(line_text):
                    header_footer_lines.add(line_text)

        if not header_footer_lines:
            return text

        # 过滤掉匹配的页眉页脚行
        filtered = []
        for line in lines:
            if line.strip() in header_footer_lines:
                continue
            filtered.append(line)

        return '\n'.join(filtered)

    @staticmethod
    def _is_likely_header_footer(text: str) -> bool:
        """
        判断文本是否像页眉页脚（而非 Markdown 内容元素）

        排除 Markdown 标题、列表、表格、代码块等结构元素，
        这些即使重复出现也不应被当作页眉页脚删除。
        """
        stripped = text.strip()

        # 排除 Markdown 标题
        if stripped.startswith('#'):
            return False
        # 排除列表项
        if stripped.startswith(('- ', '* ', '+ ', '1. ', '2. ', '3. ')):
            return False
        # 排除表格行
        if stripped.startswith('|') and stripped.count('|') >= 2:
            return False
        # 排除代码块标记
        if stripped.startswith('```'):
            return False
        # 排除水平线（含变体）
        if stripped in ('---', '***', '___', '- - -', '* * *'):
            return False
        # 排除加粗文本行
        if stripped.startswith('**') and stripped.endswith('**'):
            return False
        # 排除引用块
        if stripped.startswith('>'):
            return False
        # 排除图片
        if stripped.startswith('!['):
            return False
        # 排除过短的行（可能是编号或标记）
        if len(stripped) < 3:
            return False

        return True
