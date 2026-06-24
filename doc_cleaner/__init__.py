"""
Markdown 文档数据清洗工具包

提供 Markdown 文档的清洗功能，包括：
- 去噪（移除页眉、页脚、页码等无关内容）
- 编码标准化（统一字符编码、全半角标点转换）
- 表格处理（HTML 表格转 Markdown、表格格式规范化）
- 错误修复（修复排版断裂、错误标题识别）
- 去重（移除重复段落）
- 格式标准化（统一 Markdown 格式规范）
- 逻辑关联分析（自动分析章节间的逻辑关系）
- 段落摘要（使用 LLM 生成文档和章节摘要）
"""

from .cleaner import MarkdownCleaner

__version__ = "0.3.0"
__author__ = "Wu Hao"
__email__ = "i_net_sky@hotmail.com"
