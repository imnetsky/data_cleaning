"""
工具模块 - 提供配置管理、文件读写、API 客户端等通用功能

包含以下子模块：
- config: 配置文件的加载和管理
- file_io: 文件读写和目录扫描
- excel_converter: Excel 文件转 Markdown
- llm_client: LLM API 客户端（用于文档摘要和逻辑分析）
- mineru_client: MinerU API 客户端（用于将 PDF/Word 等非 Markdown 文件转换为 Markdown）
- logger: 日志记录（同时输出到控制台和日志文件）
"""

import os


def ensure_dir_exists(path: str) -> None:
    """确保目录存在，不存在则创建"""
    os.makedirs(path, exist_ok=True)


def get_relative_path(file_path: str, base_dir: str) -> str:
    """获取文件相对于基础目录的相对路径"""
    return os.path.relpath(file_path, base_dir)
