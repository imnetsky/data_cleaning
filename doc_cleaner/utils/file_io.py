"""
文件读写模块 - 封装文件 I/O 操作

提供统一的文件读写接口，自动处理：
- 多种编码格式的回退读取（UTF-8, GBK, GB2312, GB18030）
- 目录扫描和文件分类
- 输出目录自动创建
"""

import os
from typing import List, Optional


def read_file(file_path: str) -> str:
    """
    读取文件内容，自动尝试多种编码

    按优先级依次尝试：UTF-8 → GBK → GB2312 → GB18030，
    在 Windows 中文环境下可正确读取绝大多数文件。

    Args:
        file_path: 文件路径

    Returns:
        文件内容字符串

    Raises:
        FileNotFoundError: 文件不存在
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"文件不存在：{file_path}")

    # 按优先级尝试的编码列表
    encodings = ['utf-8', 'gbk', 'gb2312', 'gb18030']

    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            continue
        except Exception as e:
            raise IOError(f"读取文件 {file_path} 失败：{e}")

    raise UnicodeError(f"无法解码文件：{file_path}，已尝试编码：{', '.join(encodings)}")


def write_file(content: str, file_path: str) -> None:
    """
    写入文件，自动创建父目录

    使用 UTF-8 编码写入文件。如果文件的父目录不存在，则自动创建。

    Args:
        content: 要写入的内容
        file_path: 输出文件路径
    """
    # 确保输出目录存在
    output_dir = os.path.dirname(file_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def list_markdown_files(directory: str, recursive: bool = True) -> List[str]:
    """
    列出目录下的所有 Markdown 文件

    支持扩展名：.md, .markdown
    返回文件的完整绝对路径。

    Args:
        directory: 要扫描的目录
        recursive: 是否递归扫描子目录，默认为 True

    Returns:
        Markdown 文件路径列表
    """
    return _list_files_by_extension(directory, ['.md', '.markdown'], recursive)


def list_mineru_files(directory: str, recursive: bool = True) -> List[str]:
    """
    列出需要经过 MinerU 处理的非 Markdown 文档文件

    包含常见的文档格式：PDF、Word、PPT、图片等。

    Args:
        directory: 要扫描的目录
        recursive: 是否递归扫描子目录，默认为 True

    Returns:
        非 Markdown 文档文件路径列表
    """
    extensions = [
        '.pdf', '.doc', '.docx', '.ppt', '.pptx',
        '.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif',
        '.xps', '.epub', '.html', '.htm',
    ]
    return _list_files_by_extension(directory, extensions, recursive)


def list_excel_files(directory: str, recursive: bool = True) -> List[str]:
    """
    列出目录下的 Excel 文件

    Args:
        directory: 要扫描的目录
        recursive: 是否递归扫描子目录，默认为 True

    Returns:
        Excel 文件路径列表
    """
    return _list_files_by_extension(directory, ['.xlsx', '.xls'], recursive)


def list_non_markdown_files(directory: str, recursive: bool = True) -> List[str]:
    """
    列出既非 Markdown 也非 Excel 且需要 MinerU 转换的其他文件

    用于扫描需要特殊转换处理的所有文件。

    Args:
        directory: 要扫描的目录
        recursive: 是否递归扫描子目录，默认为 True

    Returns:
        非 Markdown/Excel 文件路径列表
    """
    extensions = [
        '.pdf', '.doc', '.docx', '.ppt', '.pptx',
        '.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif',
        '.xps', '.epub', '.html', '.htm',
    ]
    return _list_files_by_extension(directory, extensions, recursive)


def _list_files_by_extension(directory: str, extensions: List[str], recursive: bool = True) -> List[str]:
    """
    按扩展名过滤目录中的文件（通用方法）

    返回值经过排序以确保处理顺序一致。

    Args:
        directory: 要扫描的目录
        extensions: 要匹配的扩展名列表（含点号，如 ['.md', '.pdf']）
        recursive: 是否递归扫描子目录，默认为 True

    Returns:
        匹配的文件路径列表
    """
    if not os.path.exists(directory):
        return []

    files = []
    if recursive:
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                ext = os.path.splitext(filename)[1].lower()
                if ext in extensions:
                    files.append(os.path.join(root, filename))
    else:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                ext = os.path.splitext(filename)[1].lower()
                if ext in extensions:
                    files.append(filepath)

    return sorted(files)
