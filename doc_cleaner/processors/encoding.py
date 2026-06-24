"""
编码处理器 - 标准化字符编码、符号和换行符

处理内容包括：
- 移除零宽字符等不可见字符
- 标准化数学符号等特殊字符
- 根据上下文语境转换全半角标点
- 确保输出有效的 UTF-8 编码
"""

import re


class EncodingProcessor:
    """统一编码、不可见字符、换行符和标点符号"""

    # 中文语境下的英文/半角标点 -> 对应中文全角标点
    # 仅在标点前后均为中文字符时才替换，避免误改代码或英文内容
    _CN_PUNCT_MAP = {
        ',': '，',
        '.': '。',
        '?': '？',
        '!': '！',
        ':': '：',
        ';': '；',
        '(': '（',
        ')': '）',
    }

    # 英文语境下的中文全角标点 -> 对应半角标点
    # 仅在标点前后均为 ASCII 字母/数字时才替换
    _EN_PUNCT_MAP = {
        '，': ',',
        '。': '.',
        '？': '?',
        '！': '!',
        '：': ':',
        '；': ';',
        '（': '(',
        '）': ')',
    }

    def process(self, content: str) -> str:
        """应用编码标准化操作"""
        result = content

        # 统一换行符为 \n
        result = result.replace('\r\n', '\n').replace('\r', '\n')

        # 移除零宽空格等不可见字符
        result = self._remove_invisible_chars(result)

        # 标准化数学符号和格式符号（OCR 常见误识别字符）
        result = self._normalize_special_symbols(result)

        # 根据上下文语境统一全半角标点
        result = self._normalize_punctuation(result)

        # 确保输出有效的 UTF-8 编码
        result = self._ensure_valid_utf8(result)

        return result

    def _remove_invisible_chars(self, text: str) -> str:
        """移除零宽空格、软连字符等不可见字符"""
        # 常见的不可见 Unicode 字符列表
        invisible_chars = [
            '\u200b',  # 零宽空格 (Zero Width Space)
            '\u200c',  # 零宽非连接符 (Zero Width Non-Joiner)
            '\u200d',  # 零宽连接符 (Zero Width Joiner)
            '\u2060',  # 词连接符 (Word Joiner)
            '\ufeff',  # 字节顺序标记 (BOM)
        ]
        for char in invisible_chars:
            text = text.replace(char, '')
        return text

    def _normalize_special_symbols(self, text: str) -> str:
        """标准化数学符号和格式符号，这些符号常由 OCR 误识别产生"""
        symbol_map = {
            '\u2261': '=',      # 恒等于 ≡ -> =
            '\u2254': ':=',     # 定义为 ≔ -> :=
            '\u2260': '!=',     # 不等于 ≠ -> !=
            '\u2264': '<=',     # 小于等于 ≤ -> <=
            '\u2265': '>=',     # 大于等于 ≥ -> >=
            '\u00a0': ' ',      # 不间断空格 -> 普通空格
            '\u3000': ' ',      # 全角空格 -> 普通空格
        }
        for full, half in symbol_map.items():
            text = text.replace(full, half)
        return text

    def _normalize_punctuation(self, text: str) -> str:
        """
        根据上下文语境统一全半角标点

        规则：
        - 中文间的半角标点 -> 全角标点
        - ASCII 字符间的全角标点 -> 半角标点
        - 跳过代码块和内联代码，避免破坏语法
        """
        # 分离代码块和内联代码，避免修改其中的标点
        code_blocks: list = []
        placeholder = '__ENC_PUNCT_7f3a_{}_BLOCK__'

        def save_code(m: re.Match) -> str:
            idx = len(code_blocks)
            code_blocks.append(m.group(0))
            return placeholder.format(idx)

        # 先匹配围栏代码块，再匹配内联代码
        result = re.sub(r'```[\s\S]*?```', save_code, text)
        result = re.sub(r'`[^`\n]+`', save_code, result)

        # 半角 -> 全角：标点前后都是中文字符时转换
        cn_char = r'[\u4e00-\u9fff\u3400-\u4dbf\uff00-\uffef\u3000-\u303f]'
        for half, full in self._CN_PUNCT_MAP.items():
            pattern = f'(?<={cn_char}){re.escape(half)}(?={cn_char})'
            result = re.sub(pattern, full, result)

        # 全角 -> 半角：标点前后都是 ASCII 字母/数字时转换
        ascii_char = r'[A-Za-z0-9]'
        for full, half in self._EN_PUNCT_MAP.items():
            pattern = f'(?<={ascii_char}){re.escape(full)}(?={ascii_char})'
            result = re.sub(pattern, half, result)

        # 恢复代码块
        for idx, block in enumerate(code_blocks):
            result = result.replace(placeholder.format(idx), block)

        return result

    def _ensure_valid_utf8(self, text: str) -> str:
        """确保字符串为有效的 UTF-8 编码，无法解码的字符用替代符替换"""
        try:
            return text.encode('utf-8').decode('utf-8')
        except UnicodeError:
            return text.encode('utf-8', errors='replace').decode('utf-8')
