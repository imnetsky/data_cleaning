"""
本地文件转换模块

提供多种文件格式的本地转换能力，作为 MinerU API 的备用方案。

支持格式：
- DOCX: 复用 docx_converter 模块
- PDF: 使用 pdfplumber

注意：Excel 文件在 main.py 中通过 pandas 单独处理（excel_converter），
不经过本地转换回退路径。
"""

import os
from typing import Optional


def convert_file_to_markdown(file_path: str) -> Optional[str]:
    """
    将文件转换为 Markdown 格式

    根据文件扩展名自动选择合适的转换方法。

    Args:
        file_path: 文件路径

    Returns:
        Markdown 文本，如果转换失败或不支持的格式返回 None
    """
    if not os.path.exists(file_path):
        return None

    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.docx':
        return _convert_docx_to_markdown(file_path)
    elif ext == '.doc':
        # .doc 是旧版二进制格式，python-docx 不支持，需通过 MinerU 转换
        return None
    elif ext == '.pdf':
        return _convert_pdf_to_markdown(file_path)
    else:
        return None


def _convert_docx_to_markdown(file_path: str) -> Optional[str]:
    """将 DOCX 文件转换为 Markdown，复用 docx_converter 模块"""
    try:
        from .docx_converter import convert_docx_to_markdown
        return convert_docx_to_markdown(file_path)
    except ImportError:
        return None


def _convert_pdf_to_markdown(file_path: str) -> Optional[str]:
    """将 PDF 文件转换为 Markdown"""
    try:
        import pdfplumber

        with pdfplumber.open(file_path) as pdf:
            result = []

            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text = _clean_pdf_text(text)
                    result.append(text)

            return '\n\n'.join(result)

    except Exception as e:
        return None


def _clean_pdf_text(text: str) -> str:
    """清理 PDF 提取的文本"""
    lines = text.split('\n')
    cleaned = []

    for line in lines:
        line = line.strip()
        if line:
            cleaned.append(line)

    return '\n'.join(cleaned)
