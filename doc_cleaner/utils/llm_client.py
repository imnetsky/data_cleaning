"""
LLM 客户端模块 - 封装大语言模型 API 调用

基于 OpenAI 兼容接口封装，提供：
- 通用文本生成接口（generate）
- 文档概要生成（summarize_document）
- 章节摘要生成（summarize_section）
- 逻辑关系分析（analyze_logical_relations）
- 自动去除模型思考内容（think 标签）
"""

from openai import OpenAI
from ..utils.config import get_config
from ..utils.logger import get_logger
from typing import Optional


class LLMClient:
    """
    大语言模型（LLM）API 客户端

    封装 OpenAI 兼容接口的调用逻辑，
    包括请求构建、响应解析和错误处理。
    """

    def __init__(self, api_key: str, base_url: str, model: str, timeout: int = 120, max_tokens: int = 8192):
        """
        初始化 LLM 客户端

        Args:
            api_key: API 密钥
            base_url: API 基础地址
            model: 模型名称
            timeout: 请求超时时间（秒），默认 120
            max_tokens: 默认最大生成 Token 数，默认 8192
        """
        self.client = OpenAI(api_key=api_key, base_url=base_url, timeout=timeout)
        self.model = model
        self.default_max_tokens = max_tokens

    def generate(self, system_prompt: str, user_prompt: str,
                 max_tokens: Optional[int] = None, temperature: Optional[float] = None) -> Optional[str]:
        """
        通用文本生成方法

        向 LLM 发送系统提示和用户提示，返回模型生成的文本。
        自动去除可能的 思考标签内容。

        Args:
            system_prompt: 系统提示词，设定模型角色和行为
            user_prompt: 用户提示词，指定生成任务
            max_tokens: 最大生成 Token 数（None 时使用客户端默认值）
            temperature: 生成温度（None 时使用配置默认值）

        Returns:
            生成的文本，失败返回 None
        """
        if temperature is None:
            temperature = get_config()['llm']['temperature']

        if max_tokens is None:
            max_tokens = self.default_max_tokens

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )

            content = response.choices[0].message.content
            if content:
                content = self._remove_think_block(content)
            return content

        except Exception as e:
            logger = get_logger()
            logger.error(f"LLM API 调用失败：{e}")
            return None

    def summarize_document(self, content: str, max_length: int = 3000) -> Optional[str]:
        """
        生成文档概要

        取文档前 max_length 字符进行分析，生成简短的文档摘要。

        Args:
            content: 文档全文
            max_length: 分析用的字符数上限

        Returns:
            文档概要文本
        """
        system_prompt = "你是一个专业的文档摘要生成助手。请根据文档内容生成简洁的概要说明。"
        user_prompt = f"""请为以下文档生成概要说明（200字符以内）：

{content[:max_length]}

请以"文档概要："开头。"""

        result = self.generate(system_prompt, user_prompt, max_tokens=1024)

        # 硬性截断：确保文档概要不超过 200 字符
        if result and len(result) > 200:
            result = result[:197] + '...'

        return result

    def summarize_section(self, section_title: str, section_content: str) -> Optional[str]:
        """
        生成章节摘要

        分析指定章节的内容，生成该章节的概要描述。

        Args:
            section_title: 章节标题
            section_content: 章节正文

        Returns:
            章节概要文本
        """
        system_prompt = "你是一个专业的文档章节摘要助手。请根据章节内容生成简洁的摘要。"
        user_prompt = f"""请为章节 "{section_title}" 生成简洁的摘要（50字以内）：

{section_content[:1000]}

请以"本章概要："开头。"""

        result = self.generate(system_prompt, user_prompt, max_tokens=512)

        # 硬性截断：确保章节摘要不超过 50 字符
        if result and len(result) > 50:
            result = result[:47] + '...'

        return result

    def summarize_sections_batch(self, sections: list, content: str) -> Optional[str]:
        """
        批量生成多个章节的摘要

        将所有章节标题和前部内容合并为一次 LLM 调用，
        显著减少 API 请求次数。

        Args:
            sections: 章节列表，每个元素为 {'title': str, ...}
            content: 文档全文

        Returns:
            批量摘要文本
        """
        system_prompt = "你是一个专业的文档章节摘要助手。请为每个章节生成简洁的摘要。"
        titles_text = '\n'.join(f"{i+1}. {s['title']}" for i, s in enumerate(sections))
        user_prompt = f"""请为以下文档的各个章节分别生成简洁的摘要（每个50字以内）：

章节列表：
{titles_text}

文档内容（前3000字）：
{content[:3000]}

请按以下格式输出，每行一个章节的摘要：
章节名：本章概要内容

请以"各章节摘要："开头。"""

        return self.generate(system_prompt, user_prompt, max_tokens=2048)

    def analyze_logical_relations(self, section_titles: list) -> Optional[str]:
        """
        分析文档章节间的逻辑关系

        根据章节标题列表分析前置依赖、后续应用等逻辑关系。

        Args:
            section_titles: 章节标题列表

        Returns:
            逻辑关系分析文本
        """
        system_prompt = "你是一个专业的文档结构分析助手。请按章节分别分析逻辑关系。"
        titles_text = '\n'.join(f"- {t}" for t in section_titles)
        user_prompt = f"""请分析以下文档各章节之间的逻辑关系，按章节分别说明：

{titles_text}

请按以下格式，为每个章节说明其与其他章节的关联关系：
章节名：该章节与哪些章节有关联，是什么关系（如前置依赖、后续应用、因果关系等）

请以"逻辑关联分析："开头。"""

        return self.generate(system_prompt, user_prompt, max_tokens=1024)

    def _remove_think_block(self, content: str) -> str:
        """
        去除模型返回的思考内容标签块

        某些模型（如 DeepSeek）会在回复中包含 <think...</think:> 的思考过程，
        此方法将其移除，只保留最终的回复内容。

        Args:
            content: 原始回复文本

        Returns:
            去除思考块后的文本
        """
        import re
        cleaned = re.sub(r'<think[\s\S]*?</think\s*>', '', content)
        return cleaned.strip()
