"""
错误修复处理器 - 修复常见的 Markdown 排版错误

处理内容包括：
- 修复被误识别为 Markdown 标题的代码注释
- 修复跨行断裂的标题
- 修复跨段落断裂的句子
- 合并 PDF 转换产生的多余换行
- 修复行首多余空格
- 确保代码块前后有空行
"""

import re


class ErrorProcessor:
    """检测并修复不合理的换行、恢复段落边界"""

    def process(self, content: str) -> str:
        """应用错误修复操作"""
        result = content

        # 确保代码块前后有空行
        result = self._preserve_code_blocks(result)

        # 修复被误认为 Markdown 标题的 Shell 命令注释
        result = self._fix_code_comment_headings(result)

        # 修复断裂的标题
        result = self._fix_broken_headings(result)

        # 合并段落内的断裂行和多余换行（PDF 转换常见问题）
        result = self._fix_paragraph_breaks(result)

        # 修复行首多余空格
        result = self._fix_line_start_spaces(result)

        return result

    def _fix_code_comment_headings(self, text: str) -> str:
        """
        修复看起来像 Markdown 标题但实际是代码注释的行

        例如 '# systemctl start httpd' 是 Shell 注释，而非 Markdown 标题，
        通过在前面添加反斜杠将其转义为纯文本。

        判断规则：仅当标题内容以命令开头且后续紧跟命令参数（非中文字符）时才转义，
        避免误伤 '# systemctl 命令使用指南' 这类合法标题。
        """
        code_comment_pattern = re.compile(
            r'^(#{1,6})\s+('
            r'systemctl\s+'
            r'|yum\s+(install|remove|update|localinstall|clean|repolist|list|search|info|check-update|groupinstall|provides|reinstall|downgrade|autoremove|swap|makecache)\s'
            r'|subscription-manager\s+'
            r'|reposync\s+'
            r'|ssh[\s-]'
            r'|scp\s+'
            r'|crontab\s+'
            r'|Firewall-cmd\s+'
            r'|Systemctl\s+'
            r'|Vim\s+'
            r'|In\s+-s\s+'
            r'|tar\s+'
            r'|cd\s+'
            r'|cat\s+'
            r'|wget\s+'
            r'|ansible-playbook\s+'
            r'|ssh-keygen'
            r'|ssh-copy-id'
            r'|/etc/'
            r'|/var/'
            r'|/data/'
            r'|/home/'
            r'|http://'
            r'|https://'
            r')',
            re.IGNORECASE
        )

        lines = text.split('\n')
        result = []
        in_code_block = False

        for line in lines:
            stripped = line.strip()

            if stripped.startswith('```'):
                in_code_block = not in_code_block
                result.append(line)
                continue

            if in_code_block:
                result.append(line)
                continue

            if code_comment_pattern.match(stripped):
                # 提取标题文本部分（# 之后的内容）
                heading_text = stripped.lstrip('#').strip()
                # 仅当标题文本不含中文字符时才视为代码注释并转义
                # 含中文字符的标题（如 "# systemctl 命令使用指南"）是合法标题，不转义
                if not re.search(r'[\u4e00-\u9fff\u3400-\u4dbf]', heading_text):
                    result.append('\\' + stripped)
                    continue

            result.append(line)

        return '\n'.join(result)

    def _fix_broken_headings(self, text: str) -> str:
        """
        修复跨行断裂的标题

        示例：将 "# 三、\n\n防火\n\n# 墙开通需求" 合并为 "# 三、防火墙开通需求"
        仅当标题明显不完整（如只有序号没有内容）时才进行合并
        """
        lines = text.split('\n')
        result_lines = []
        in_code_block = False
        i = 0

        # 匹配不完整的标题模式：仅有"一、"、"二、"等中文序号
        incomplete_heading_pattern = re.compile(
            r'^[一二三四五六七八九十]+[、.]$'
        )

        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            if stripped.startswith('```'):
                in_code_block = not in_code_block
                result_lines.append(line)
                i += 1
                continue

            if in_code_block:
                result_lines.append(line)
                i += 1
                continue

            if stripped.startswith('#') and re.match(r'^#{1,6}\s+\S', stripped):
                heading_text = stripped.lstrip('#').strip()

                # 检测到不完整的标题（如 "# 三、"），尝试与后续内容合并
                if incomplete_heading_pattern.match(heading_text):
                    is_broken = False
                    j = i + 1

                    # 跳过空行
                    while j < len(lines) and not lines[j].strip():
                        j += 1

                    if j < len(lines):
                        next_line = lines[j].strip()

                        # 检查后续行是否为标题的一部分（非块级元素且较短）
                        if (not next_line.startswith('#') and
                            not next_line.startswith('|') and
                            not next_line.startswith('```') and
                            not next_line.startswith('- ') and
                            not next_line.startswith('![') and
                            len(next_line) < 20 and
                            re.match(r'^[\u4e00-\u9fff\w]', next_line)):

                            k = j + 1
                            while k < len(lines) and not lines[k].strip():
                                k += 1

                            # 再往后检查是否有另一个断裂的标题片段
                            if k < len(lines):
                                after_next = lines[k].strip()
                                if after_next.startswith('#') and re.match(r'^#{1,6}\s+\S', after_next):
                                    after_next_text = after_next.lstrip('#').strip()
                                    if len(after_next_text) < 20 and re.match(r'^[\u4e00-\u9fff\w]', after_next_text):
                                        # 将三个断裂部分合并为一个标题
                                        merged = stripped[:len(stripped) - len(stripped.lstrip('#'))] + ' ' + heading_text + next_line + after_next_text
                                        result_lines.append(merged)
                                        i = k + 1
                                        is_broken = True

                            if not is_broken:
                                # 将标题和下一个内容合并
                                merged = stripped[:len(stripped) - len(stripped.lstrip('#'))] + ' ' + heading_text + next_line
                                result_lines.append(merged)
                                i = j + 1
                                is_broken = True

                    if not is_broken:
                        result_lines.append(line)
                        i += 1
                else:
                    result_lines.append(line)
                    i += 1
            else:
                result_lines.append(line)
                i += 1

        return '\n'.join(result_lines)

    def _fix_paragraph_breaks(self, text: str) -> str:
        """
        合并段落内的断裂行和多余换行

        统一处理两类问题（合并自 _fix_broken_sentences 和 _fix_single_newlines）：
        1. 跨空行的断句：空行前一行不以终止符结尾，空行后是合法续行，则删除空行
        2. 段落内的单个换行：同一段落中间的单独换行，替换为空格
        不在代码块内生效。
        """
        lines = text.split('\n')
        result_lines = []
        in_code_block = False

        for i, line in enumerate(lines):
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                result_lines.append(line)
                continue

            if in_code_block:
                result_lines.append(line)
                continue

            if self._is_blank_line(line):
                if result_lines:
                    last_line = result_lines[-1]
                    if not self._is_blank_line(last_line) and not self._is_markdown_block_element(last_line):
                        prev_text = last_line.rstrip()
                        next_idx = i + 1
                        next_is_continuation = False
                        if next_idx < len(lines):
                            next_line = lines[next_idx].strip()
                            if (next_line
                                and not self._is_markdown_block_element(lines[next_idx])
                                and not self._is_blank_line(lines[next_idx])):
                                next_is_continuation = True
                        prev_ends_mid = not re.search(r'[.!?。！？;；:："\'）\)」』]$', prev_text)
                        if prev_ends_mid and next_is_continuation:
                            continue
                result_lines.append(line)
                continue

            if self._is_markdown_block_element(line):
                result_lines.append(line)
                continue

            if result_lines:
                last_line = result_lines[-1]
                if not self._is_blank_line(last_line) and not self._is_markdown_block_element(last_line):
                    prev_text = last_line.rstrip()
                    curr_text = line.strip()
                    if prev_text and curr_text:
                        prev_ends_mid = not re.search(r'[.!?。！？;；:："\'）\)」』]$', prev_text)
                        curr_starts_continuation = re.match(r'^[a-z\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', curr_text)
                        if prev_ends_mid and curr_starts_continuation:
                            result_lines[-1] = prev_text + ' ' + curr_text
                            continue

            result_lines.append(line)

        return '\n'.join(result_lines)

    def _is_markdown_block_element(self, line: str) -> bool:
        """检查行是否为 Markdown 块级元素的开头"""
        stripped = line.strip()
        if stripped.startswith('#'):
            return True
        if stripped.startswith(('- ', '* ', '+ ', '1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
            return True
        if stripped.startswith('```'):
            return True
        if stripped in ('---', '***', '___'):
            return True
        if stripped.startswith('|'):
            return True
        if stripped.startswith('>'):
            return True
        if stripped.startswith('!['):
            return True
        return False

    def _is_blank_line(self, line: str) -> bool:
        """检查行是否为空白行"""
        return not line.strip()

    def _fix_line_start_spaces(self, text: str) -> str:
        """
        修复行首多余空格

        保留列表项的必要缩进（最多 3 个空格），
        普通文本行移除行首多余空格。
        """
        lines = text.split('\n')
        result = []
        in_code_block = False

        for line in lines:
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                result.append(line)
                continue

            if in_code_block:
                result.append(line)
                continue

            stripped = line.lstrip()
            # 列表项：保留最多 3 个空格的缩进
            if stripped.startswith(('- ', '* ', '+ ', '1. ', '2. ', '3. ', '4. ', '5. ', '6. ', '7. ', '8. ', '9. ')):
                leading_spaces = len(line) - len(stripped)
                preserve = min(leading_spaces, 3)
                result.append(' ' * preserve + stripped)
            else:
                result.append(stripped)

        return '\n'.join(result)

    def _preserve_code_blocks(self, text: str) -> str:
        """确保代码块前后有空行，保证 Markdown 格式正确"""
        lines = text.split('\n')
        result = []
        in_code_block = False

        for i, line in enumerate(lines):
            if line.strip().startswith('```'):
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
            elif in_code_block:
                result.append(line)
            else:
                result.append(line)

        return '\n'.join(result)
