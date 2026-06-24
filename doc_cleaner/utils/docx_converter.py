"""
DOCX 文件转换模块

使用 python-docx 库将 DOCX 文件转换为 Markdown 格式，
作为 MinerU API 的备用方案。
"""

from typing import Optional
from docx import Document
from docx.table import Table


def convert_docx_to_markdown(file_path: str) -> Optional[str]:
    """
    将 DOCX 文件转换为 Markdown 格式

    Args:
        file_path: DOCX 文件路径

    Returns:
        Markdown 文本，如果转换失败返回 None
    """
    try:
        doc = Document(file_path)
        result = []

        for element in doc.element.body:
            if element.tag.endswith('p'):
                paragraph = element
                text = _parse_paragraph(paragraph)
                if text:
                    result.append(text)
            elif element.tag.endswith('tbl'):
                table = Table(element, doc)
                markdown_table = _parse_table(table)
                if markdown_table:
                    result.append(markdown_table)

        return '\n\n'.join(result)

    except Exception as e:
        logger = _get_logger()
        logger.error(f"DOCX 转换失败：{e}")
        return None


def _parse_paragraph(paragraph_element) -> str:
    """解析段落元素"""
    text = ''
    for child in paragraph_element:
        if child.tag.endswith('r'):
            run_text = ''
            for inner in child:
                if inner.tag.endswith('t'):
                    run_text += inner.text or ''
            if run_text:
                text += run_text

    if not text.strip():
        return ''

    style = paragraph_element.get('w:style')
    if style:
        style_name = style.split('}')[-1] if '}' in style else style
        if style_name.startswith('Heading1') or style_name.startswith('标题1'):
            return f'# {text.strip()}'
        elif style_name.startswith('Heading2') or style_name.startswith('标题2'):
            return f'## {text.strip()}'
        elif style_name.startswith('Heading3') or style_name.startswith('标题3'):
            return f'### {text.strip()}'
        elif style_name.startswith('Heading4') or style_name.startswith('标题4'):
            return f'#### {text.strip()}'
        elif style_name.startswith('Heading5') or style_name.startswith('标题5'):
            return f'##### {text.strip()}'
        elif style_name.startswith('Heading6') or style_name.startswith('标题6'):
            return f'###### {text.strip()}'

    return text.strip()


def _parse_table(table: Table) -> str:
    """解析表格元素"""
    rows = []
    for i, row in enumerate(table.rows):
        cells = []
        for cell in row.cells:
            text = '\n'.join(p.text.strip() for p in cell.paragraphs if p.text.strip())
            cells.append(text)
        if any(cells):
            rows.append(cells)

    if not rows:
        return ''

    markdown_rows = []
    for i, row in enumerate(rows):
        markdown_rows.append('| ' + ' | '.join(row) + ' |')
        if i == 0:
            markdown_rows.append('| ' + ' | '.join(['---'] * len(row)) + ' |')

    return '\n'.join(markdown_rows)


def _get_logger():
    """获取日志记录器"""
    import logging
    return logging.getLogger(__name__)
