"""
处理器模块 - 文档清洗的各种处理器实现

所有处理器遵循统一的接口规范：
每个处理器类都包含 process(self, content: str) -> str 方法，
输入原始 Markdown 文本，返回处理后的 Markdown 文本。
"""

from .denoise import DenoiseProcessor
from .encoding import EncodingProcessor
from .tables import TableProcessor
from .dedup import DedupProcessor
from .errors import ErrorProcessor
from .segment_intro import SegmentIntroProcessor
from .format_standardization import FormatStandardizationProcessor

__all__ = [
    'DenoiseProcessor',
    'EncodingProcessor',
    'TableProcessor',
    'DedupProcessor',
    'ErrorProcessor',
    'SegmentIntroProcessor',
    'FormatStandardizationProcessor',
]
