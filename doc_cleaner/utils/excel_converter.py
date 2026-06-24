"""
Excel 转换器 - 将 Excel 文件转换为 Markdown 表格格式

将 .xlsx/.xls 文件中的每个工作表（sheet）转换为 Markdown 表格，
支持多个工作表，并用标题区分。
"""

import pandas as pd
from .logger import get_logger
from typing import Optional

logger = get_logger()


def excel_to_markdown(file_path: str, max_sheets: int = 10) -> Optional[str]:
    """
    将 Excel 文件转换为 Markdown 格式

    读取 Excel 文件的所有工作表，每个工作表转换后格式为：
    ```
    ## [工作表名称]
    | 列1 | 列2 | ... |
    | --- | --- | ... |
    | 值1 | 值2 | ... |
    ```

    Args:
        file_path: Excel 文件路径（.xlsx 或 .xls）
        max_sheets: 最大处理的工作表数，超出则截断

    Returns:
        Markdown 格式文本，失败返回 None
    """
    try:
        # 读取 Excel 文件，获取所有工作表名称
        xls = pd.ExcelFile(file_path)
        sheet_names = xls.sheet_names[:max_sheets]
    except Exception as e:
        logger.error(f"读取 Excel 文件失败：{e}")
        return None

    markdown_parts = []

    for sheet_name in sheet_names:
        try:
            # 读取工作表数据
            df = pd.read_excel(file_path, sheet_name=sheet_name)

            # 跳过空工作表
            if df.empty:
                continue

            # 添加工作表名称作为 Markdown 标题
            markdown_parts.append(f"## {sheet_name}")
            markdown_parts.append("")

            # 将 DataFrame 转为 Markdown 表格
            table_lines = _dataframe_to_markdown_table(df)
            markdown_parts.extend(table_lines)
            markdown_parts.append("")

        except Exception as e:
            logger.warning(f"处理工作表 {sheet_name} 失败：{e}")
            continue

    result = '\n'.join(markdown_parts)
    return result if result.strip() else None


def _dataframe_to_markdown_table(df: pd.DataFrame) -> list:
    """
    将 pandas DataFrame 转换为 Markdown 表格格式的行列表

    自动处理缺失值（NaN 转为空字符串），
    并将所有数据列转换为字符串格式。

    Args:
        df: 要转换的 DataFrame

    Returns:
        Markdown 表格行列表，包含表头行、分隔行和数据行
    """
    lines = []

    # 处理表头：将列名转为字符串
    headers = [str(col) if col is not None else '' for col in df.columns]
    header_line = '| ' + ' | '.join(headers) + ' |'
    lines.append(header_line)

    # 构建 Markdown 表格分隔行
    separator = '| ' + ' | '.join(['---'] * len(headers)) + ' |'
    lines.append(separator)

    # 逐行处理数据，将 NaN 替换为空字符串
    for _, row in df.iterrows():
        cells = []
        for value in row:
            if pd.isna(value):
                cells.append('')
            else:
                cells.append(str(value))
        data_line = '| ' + ' | '.join(cells) + ' |'
        lines.append(data_line)

    return lines
