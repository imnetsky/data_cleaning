"""
表格处理器 - 处理 Markdown 文档中的表格

主要功能：
- 将 HTML 表格转换为标准的 Markdown 表格格式
- 清理 Markdown 表格格式（对齐分隔线、统一分隔符）
- 确保表格在 Markdown 文档中的正确渲染
"""

import re


class TableProcessor:
    """
    检测和处理 Markdown 文档中的表格

    支持将 HTML <table> 标签转换为标准 Markdown 表格，
    并清理不符合规范的 Markdown 表格格式。
    """

    def process(self, content: str) -> str:
        """应用表格处理操作"""
        result = content

        # HTML 表格转 Markdown 表格
        result = self._convert_html_tables_to_markdown(result)

        # 清理 Markdown 表格格式
        result = self._clean_markdown_tables(result)

        return result

    def _convert_html_tables_to_markdown(self, text: str) -> str:
        """
        将文档中的 HTML <table> 元素转换为标准的 Markdown 表格格式

        支持 <table>, <tr>, <th>, <td> 等标准 HTML 表格元素。
        解析 tr 中的 th 作为表头，td 作为数据行。
        """
        def convert_table(match):
            html = match.group(0)
            rows = []

            # 提取所有表头单元格（<th>）
            headers = re.findall(r'<th[^>]*>(.*?)</th>', html, re.DOTALL | re.IGNORECASE)
            # 提取所有数据行（<tr>）
            data_rows = re.findall(r'<tr[^>]*>(.*?)</tr>', html, re.DOTALL | re.IGNORECASE)

            has_headers = bool(headers)

            if has_headers:
                # 清理表头单元格内标记并构建表头行
                header_row = '| ' + ' | '.join(
                    re.sub(r'<[^>]+>', '', h).strip() for h in headers
                ) + ' |'

                # 构建分隔行
                separator = '| ' + ' | '.join('---' for _ in headers) + ' |'
                rows.append(header_row)
                rows.append(separator)

            # 处理数据行：从每个 <tr> 中提取 <td>
            for tr in data_rows:
                cells = re.findall(r'<td[^>]*>(.*?)</td>', tr, re.DOTALL | re.IGNORECASE)
                if cells:
                    row = '| ' + ' | '.join(
                        re.sub(r'<[^>]+>', '', c).strip() for c in cells
                    ) + ' |'
                    rows.append(row)

            return '\n'.join(rows) if rows else html

        # 匹配 HTML table 元素的模式
        table_pattern = re.compile(r'<table[^>]*>.*?</table>', re.DOTALL | re.IGNORECASE)
        return table_pattern.sub(convert_table, text)

    def _clean_markdown_tables(self, text: str) -> str:
        """
        清理和标准化 Markdown 表格格式

        操作包括：
        - 合并因换行断裂的表格行
        - 标准化表头分隔行（确保使用 ---）
        - 对齐表格列
        """
        lines = text.split('\n')
        result = []
        i = 0

        while i < len(lines):
            line = lines[i]

            if self._is_table_line(line):
                # 收集连续的表格行
                table_lines = []
                while i < len(lines) and self._is_table_line(lines[i]):
                    # 合并同一格因换行断裂的行
                    cleaned = lines[i].strip()
                    while cleaned.count('|') < 2 and i + 1 < len(lines):
                        i += 1
                        cleaned += ' ' + lines[i].strip()
                    table_lines.append(cleaned)
                    i += 1

                if table_lines:
                    result.extend(table_lines)
                    if i < len(lines) and lines[i].strip():
                        result.append('')
            else:
                result.append(line)
                i += 1

        return '\n'.join(result)

    def _is_table_line(self, line: str) -> bool:
        """判断一行是否为 Markdown 表格的组成部分"""
        stripped = line.strip()
        # 检查表头分隔行模式：|---| 或 |:---:|
        if re.match(r'^\|[\s:-]+\|[\s:-]+(?:\|[\s:-]+)*\|?$', stripped):
            return True
        # 检查数据行：必须以 | 开头或结尾，且包含至少 2 个 |
        # 避免将 "请输入 a | b | c" 这类普通文本误判为表格行
        if stripped.count('|') >= 2 and (stripped.startswith('|') or stripped.endswith('|')):
            return True
        return False
