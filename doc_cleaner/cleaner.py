"""
Markdown 文档清洗器 - 协调所有处理器的执行

MarkdownCleaner 类为核心入口，按顺序执行处理器链，
支持完整清洗和基础清洗两种模式。
"""

import time
from typing import List, Callable
from .processors import (
    DenoiseProcessor,
    EncodingProcessor,
    TableProcessor,
    DedupProcessor,
    ErrorProcessor,
    SegmentIntroProcessor,
    FormatStandardizationProcessor,
)
from .utils.config import get_config, load_config
from .utils.logger import get_logger


class MarkdownCleaner:
    """Markdown 文档清洗器，按顺序执行所有处理器"""

    def __init__(self, processors: List[Callable] = None, config_path: str = None):
        """
        初始化清洗器，可传入自定义处理器列表

        Args:
            processors: 自定义处理器列表，为 None 时使用默认处理器
            config_path: 配置文件路径，为 None 时使用默认配置
        """
        if config_path:
            load_config(config_path)

        # 完整清洗处理器链：依次执行编码处理、去噪、表格处理、错误修复、去重、
        # 格式标准化、逻辑关联分析和段落摘要生成
        self.processors = processors or [
            EncodingProcessor(),
            DenoiseProcessor(),
            TableProcessor(),
            ErrorProcessor(),
            DedupProcessor(),
            FormatStandardizationProcessor(),
            SegmentIntroProcessor(),
        ]

        # 基础清洗处理器链：仅包含数据清洗，不含 LLM 处理
        # 用于 Excel 等数据型文件的清洗，不需要上下文分析
        self.basic_processors = [
            EncodingProcessor(),
            DenoiseProcessor(),
            TableProcessor(),
            ErrorProcessor(),
            DedupProcessor(),
            FormatStandardizationProcessor(),
        ]

    def clean(self, content: str) -> str:
        """
        完整清洗：应用所有处理器（含 LLM 分析）

        Args:
            content: 原始 Markdown 内容

        Returns:
            清洗后的 Markdown 内容
        """
        logger = get_logger()
        result = content
        for processor in self.processors:
            name = type(processor).__name__
            start = time.time()
            result = processor.process(result)
            elapsed = time.time() - start
            logger.info(f"  [{name}] 处理完成（{elapsed:.2f}s）")
        return result

    def clean_basic(self, content: str) -> str:
        """
        基础清洗：仅应用数据清洗处理器（不含 LLM 分析）

        适用于 Excel 等数据型文件，不需要上下文分析和文档摘要

        Args:
            content: 原始 Markdown 内容

        Returns:
            清洗后的 Markdown 内容
        """
        logger = get_logger()
        result = content
        for processor in self.basic_processors:
            name = type(processor).__name__
            start = time.time()
            result = processor.process(result)
            elapsed = time.time() - start
            logger.info(f"  [{name}] 处理完成（{elapsed:.2f}s）")
        return result

    def clean_file(self, input_path: str, output_path: str) -> None:
        """
        读取文件、清洗、写入文件的一站式方法

        Args:
            input_path: 输入文件路径
            output_path: 输出文件路径
        """
        from .utils.file_io import read_file, write_file

        content = read_file(input_path)
        cleaned = self.clean(content)
        write_file(cleaned, output_path)
