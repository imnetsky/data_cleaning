"""
日志模块 - 提供统一的日志记录功能

同时输出到控制台和日志文件：
- 控制台：显示执行进度信息
- 日志文件：写入 log/ 目录下，按时间戳命名

使用方式：
    from doc_cleaner.utils.logger import get_logger
    logger = get_logger()
    logger.info("处理文件：xxx")
"""

import os
import logging
import sys
from datetime import datetime
from typing import Optional


_logger: Optional[logging.Logger] = None
_log_dir: Optional[str] = None


def setup_logger(log_dir: Optional[str] = None, name: str = 'doc_cleaner') -> logging.Logger:
    """
    初始化日志记录器

    创建同时输出到控制台和文件的日志记录器。
    日志文件按时间戳命名，存放在 log_dir 目录下。

    Args:
        log_dir: 日志文件存放目录，默认为项目根目录下的 log/
        name: 日志记录器名称

    Returns:
        配置好的 Logger 实例
    """
    global _logger, _log_dir

    if _logger is not None:
        return _logger

    if log_dir is None:
        project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        log_dir = os.path.join(project_root, 'log')

    _log_dir = log_dir
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        _logger = logger
        return _logger

    log_format = '%(asctime)s [%(levelname)s] %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    formatter = logging.Formatter(log_format, datefmt=date_format)

    console_handler = logging.StreamHandler(
        stream=open(sys.stdout.fileno(), mode='w', encoding='utf-8', errors='replace', closefd=False)
    )
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_filename = f'clean_{timestamp}.log'
    log_filepath = os.path.join(log_dir, log_filename)

    file_handler = logging.FileHandler(log_filepath, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info(f"日志文件：{log_filepath}")

    _logger = logger
    return _logger


def get_logger() -> logging.Logger:
    """
    获取日志记录器实例

    如果尚未初始化，自动使用默认配置初始化。

    Returns:
        Logger 实例
    """
    global _logger
    if _logger is None:
        _logger = setup_logger()
    return _logger
