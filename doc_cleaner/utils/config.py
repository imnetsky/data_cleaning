"""
配置管理模块 - 加载和管理应用程序配置

提供基于 YAML 的配置加载机制，支持：
- 默认配置内置（无需配置文件即可运行）
- YAML 配置文件覆盖默认值
- 深度合并策略（用户配置只覆盖需要更改的部分）
- 安全的环境变量占位符替换
"""

import os
import logging
import yaml
from typing import Dict, Any, Optional


# 默认配置：内置合理的默认值，确保无需配置文件也可运行
_DEFAULT_CONFIG = {
    'llm': {
        'api_key': '',              # LLM API 密钥，需通过配置文件或环境变量提供
        'base_url': 'https://api.openai.com/v1',  # API 基础地址（兼容 OpenAI 接口）
        'model': 'gpt-4o-mini',     # 使用的模型名称
        'max_tokens': 8192,         # 最大 Token 数
        'temperature': 0.3,
        'timeout': 120,             # 请求超时时间（秒）
    },
    'mineru': {
        'api_key': '',              # MinerU API 密钥
        'base_url': 'https://mineru.net',  # MinerU API 基础地址
        'precision_base_url': '',   # 精准模式 API 地址
        'agent_base_url': '',       # 轻量模式 API 地址
        'callback_url': '',         # 回调 URL（异步通知）
        'mode': 'precision',        # 默认解析模式
        'model_version': 'vlm',     # 模型版本
        'batch_upload_url': 'https://mineru.net/api/v4/file-urls/batch',  # 批量上传 API 路径
        'poll_interval': 15,        # 轮询间隔（秒）
        'poll_timeout': 300,        # 轮询超时（秒）
        'fallback_local_convert': True,  # MinerU 转换失败后是否尝试本地转换
    },
    'processing': {
        'batch_size': 2,            # 批量处理的文件数
    },
}

# 保存当前生效的配置
_current_config: Dict[str, Any] = dict(_DEFAULT_CONFIG)


def load_config(config_path: str) -> Dict[str, Any]:
    """
    从 YAML 文件加载配置，与默认配置深度合并

    Args:
        config_path: YAML 配置文件路径

    Returns:
        合并后的完整配置字典
    """
    global _current_config

    if not os.path.exists(config_path):
        logging.warning(f"配置文件 {config_path} 不存在，使用默认配置")
        _current_config = dict(_DEFAULT_CONFIG)
        return _current_config

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            user_config = yaml.safe_load(f)

        if user_config is None:
            _current_config = dict(_DEFAULT_CONFIG)
            return _current_config

        # 深度合并用户配置与默认配置
        _current_config = _deep_merge(dict(_DEFAULT_CONFIG), user_config)
        return _current_config

    except Exception as e:
        logging.warning(f"加载配置文件失败 ({e})，使用默认配置")
        _current_config = dict(_DEFAULT_CONFIG)
        return _current_config


def get_config() -> Dict[str, Any]:
    """
    获取当前生效的配置

    Returns:
        当前配置字典
    """
    return _current_config


def get(key: str, default: Any = None) -> Any:
    """
    按点分隔的键路径获取配置值

    例如：get('llm.api_key') 获取 _current_config['llm']['api_key']

    Args:
        key: 点分隔的键路径
        default: 键不存在时的默认值
    """
    keys = key.split('.')
    value = _current_config
    try:
        for k in keys:
            value = value[k]
        return value
    except (KeyError, TypeError):
        return default


def _deep_merge(base: Dict, override: Dict) -> Dict:
    """
    深度合并两个字典

    override 中的值会覆盖 base 中的对应值。
    对于嵌套字典，递归合并；对于非字典值，直接覆盖。

    Args:
        base: 基础字典（默认配置）
        override: 覆盖字典（用户配置）

    Returns:
        合并后的字典
    """
    result = dict(base)

    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # 双方都是字典时递归合并
            result[key] = _deep_merge(result[key], value)
        elif isinstance(value, str) and value.startswith('${') and value.endswith('}'):
            # 替换环境变量占位符，例如 ${API_KEY}
            env_var = value[2:-1]
            result[key] = os.environ.get(env_var, result.get(key, ''))
        else:
            # 直接覆盖
            result[key] = value

    return result
