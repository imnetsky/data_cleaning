"""
MinerU 客户端模块 - 调用 MinerU API 将文档转换为 Markdown

MinerU 是一个文档转换服务，支持将 PDF、Word、PPT、图片等
多种格式的文件转换为 Markdown 格式。

支持两种转换模式：
- precision（精准模式）：高质量转换，支持单文件和批量处理
  端点：/api/v4/file-urls/batch（批量上传URL）→ /api/v4/extract-results/batch/{batch_id}（轮询）
  需要 Bearer Token，返回 ZIP（Markdown + JSON）
- agent（轻量模式）：快速转换，仅支持单文件
  端点：POST /api/v1/agent/parse/file（提交文件名）→ PUT file_url（上传文件）→ GET /api/v1/agent/parse/{task_id}（轮询）
  不需要 Token（IP 限流），返回 Markdown CDN 链接
"""

import os
import time
import requests
import zipfile
import io
from typing import Optional, List, Dict, Any
from ..utils.config import get_config
from ..utils.logger import get_logger

try:
    from .local_converter import convert_file_to_markdown
    LOCAL_CONVERTER_AVAILABLE = True
except ImportError:
    LOCAL_CONVERTER_AVAILABLE = False


class MinerUClient:
    """
    MinerU API 客户端

    提供文件上传、转换状态轮询、结果下载的一站式接口。
    支持 precision（精准）和 agent（轻量）两种转换模式。
    """

    def __init__(self, api_key: str = None, base_url: str = None,
                 precision_base_url: str = None, agent_base_url: str = None,
                 callback_url: str = None):
        """
        初始化 MinerU 客户端

        Args:
            api_key: API 密钥
            base_url: 通用基础地址
            precision_base_url: 精准模式专用地址
            agent_base_url: 轻量模式专用地址
            callback_url: 回调通知 URL
        """
        config = get_config()

        self.api_key = api_key or config['mineru']['api_key']
        self.base_url = base_url or config['mineru'].get('base_url') or 'https://mineru.net'
        self.precision_base_url = precision_base_url or config['mineru'].get('precision_base_url') or self.base_url
        self.agent_base_url = agent_base_url or config['mineru'].get('agent_base_url') or self.base_url
        self.callback_url = callback_url or config['mineru'].get('callback_url', '')

        self.batch_upload_url = config['mineru'].get('batch_upload_url', '')

        self.poll_interval = config['mineru'].get('poll_interval', 15)
        self.max_poll_time = config['mineru'].get('poll_timeout', 300)
        self.model_version = config['mineru'].get('model_version', 'vlm')

        self.fallback_local_convert = config['mineru'].get('fallback_local_convert', True)

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def convert_file(self, file_path: str, mode: str = 'precision') -> Optional[str]:
        """
        将文件转换为 Markdown 格式，支持三级回退策略

        回退顺序：
        1. 使用指定模式（precision 或 agent）调用 MinerU API
        2. 如果指定模式失败且不是 agent，则自动尝试 agent 模式
        3. 如果 agent 模式也失败，回退到本地转换（需启用 fallback_local_convert）

        Args:
            file_path: 待转换的文件路径
            mode: 转换模式，可选 'precision' 或 'agent'

        Returns:
            转换后的 Markdown 文本，失败返回 None
        """
        logger = get_logger()

        if not os.path.exists(file_path):
            logger.error(f"文件不存在：{file_path}")
            return None

        result = None

        # 第一级：使用指定模式调用 MinerU API
        if mode == 'precision':
            result = self._convert_precision(file_path)
            if result is None:
                logger.warning(f"精准模式转换失败，自动回退到 Agent 轻量模式：{os.path.basename(file_path)}")
                result = self._convert_agent(file_path)
        elif mode == 'agent':
            result = self._convert_agent(file_path)
        else:
            logger.warning(f"未知模式：{mode}，使用 precision 模式")
            result = self._convert_precision(file_path)
            if result is None:
                logger.warning(f"精准模式转换失败，自动回退到 Agent 轻量模式：{os.path.basename(file_path)}")
                result = self._convert_agent(file_path)

        # 第二级：如果 MinerU 所有模式均失败，回退到本地转换
        if result is None and self.fallback_local_convert and LOCAL_CONVERTER_AVAILABLE:
            ext = os.path.splitext(file_path)[1].lower()
            # 本地转换仅支持 DOCX 和 PDF
            # Excel 已在 main.py 中通过 pandas 单独处理
            # .doc 是旧版二进制格式，python-docx 不支持
            supported_extensions = ('.docx', '.pdf')

            if ext in supported_extensions:
                logger.info(f"MinerU 所有模式均失败，回退到本地转换 ({ext})：{file_path}")
                try:
                    result = convert_file_to_markdown(file_path)
                    if result:
                        logger.info(f"本地转换成功 ({ext})：{file_path}")
                except Exception as e:
                    logger.error(f"本地转换失败 ({ext})：{e}")

        return result

    def _convert_precision(self, file_path: str) -> Optional[str]:
        """
        精准模式转换

        步骤：
        1. 调用批量上传 API 获取文件上传 URL
        2. 上传本地文件到返回的 URL
        3. 系统自动提交转换任务
        4. 轮询批次状态直到完成
        5. 下载 ZIP 结果并提取 Markdown

        Args:
            file_path: 文件路径

        Returns:
            Markdown 文本
        """
        logger = get_logger()
        filename = os.path.basename(file_path)

        # Step 1: 获取文件上传 URL
        if self.batch_upload_url:
            upload_url_endpoint = self.batch_upload_url
        else:
            upload_url_endpoint = f"{self.precision_base_url}/api/v4/file-urls/batch"
        try:
            logger.info(f"申请上传 URL：{filename}")
            response = requests.post(
                upload_url_endpoint,
                headers=self.headers,
                json={
                    "files": [{"name": filename}],
                    "model_version": self.model_version,
                },
                timeout=30
            )

            if response.status_code != 200:
                logger.error(f"获取上传 URL 失败：{response.status_code} {response.text}")
                return None

            result = response.json()
            if result.get('code') != 0:
                logger.error(f"获取上传 URL 失败：{result.get('msg', '未知错误')}")
                return None

            batch_id = result['data']['batch_id']
            file_urls = result['data']['file_urls']
            if not file_urls:
                logger.error("未获取到上传 URL")
                return None

            upload_url = file_urls[0]

        except requests.RequestException as e:
            logger.error(f"获取上传 URL 异常：{e}")
            return None

        # Step 2: 上传文件
        try:
            logger.info(f"上传文件：{filename}")
            with open(file_path, 'rb') as f:
                upload_response = requests.put(upload_url, data=f, timeout=120)

            if upload_response.status_code != 200:
                logger.error(f"文件上传失败：{upload_response.status_code} {upload_response.text}")
                return None

            logger.info(f"文件上传成功：{filename}")

        except requests.RequestException as e:
            logger.error(f"文件上传异常：{e}")
            return None

        # Step 3: 轮询批次状态
        return self._poll_batch_result(batch_id)

    def convert_files_batch(
        self,
        file_paths: list,
        mode: str = 'precision'
    ) -> dict:
        """批量上传多个文件到 MinerU API 进行转换（真正的批量调用）

        将所有文件在一个 API 批量请求中提交，而非逐个调用。
        仅 precision 模式支持真正的批量上传；agent 模式回退到逐个转换。

        Args:
            file_paths: 文件路径列表
            mode: 转换模式，仅 'precision' 支持批量

        Returns:
            字典 {file_path: markdown_content, ...}，
            未成功转换的文件不会出现在字典中
        """
        logger = get_logger()
        if not file_paths:
            return {}

        if mode != 'precision':
            results = {}
            for fp in file_paths:
                content = self.convert_file(fp, mode=mode)
                if content is not None:
                    results[fp] = content
            return results

        # ---- precision 模式批量上传 ----
        filenames = [os.path.basename(fp) for fp in file_paths]

        if self.batch_upload_url:
            upload_url_endpoint = self.batch_upload_url
        else:
            upload_url_endpoint = (f"{self.precision_base_url}"
                                   "/api/v4/file-urls/batch")

        preview = ", ".join(filenames[:3])
        suffix = "..." if len(filenames) > 3 else ""
        logger.info(
            f"批量上传 {len(file_paths)} 个文件：{preview}{suffix}")

        try:
            response = requests.post(
                upload_url_endpoint,
                headers=self.headers,
                json={
                    "files": [{"name": fn} for fn in filenames],
                    "model_version": self.model_version,
                },
                timeout=30
            )
            if response.status_code != 200:
                logger.error(
                    f"批量上传 URL 获取失败：{response.status_code}")
                return self._batch_fallback_individual(
                    file_paths, mode, logger)

            result = response.json()
            if result.get('code') != 0:
                msg = result.get('msg', '未知错误')
                logger.error(f"批量上传 URL 获取失败：{msg}")
                return self._batch_fallback_individual(
                    file_paths, mode, logger)

            batch_id = result['data']['batch_id']
            file_urls = result['data']['file_urls']

            if len(file_urls) != len(file_paths):
                logger.warning(
                    f"返回的上传 URL 数量 ({len(file_urls)})"
                    f" 与文件数量 ({len(file_paths)}) 不一致")
                return self._batch_fallback_individual(
                    file_paths, mode, logger)

        except requests.RequestException as e:
            logger.error(f"批量上传 URL 请求异常：{e}")
            return self._batch_fallback_individual(
                file_paths, mode, logger)

        # Step 2: 上传所有文件到各自的预签名 URL
        upload_success = []
        for i, (fp, upload_url) in enumerate(zip(file_paths, file_urls)):
            try:
                n = i + 1
                total = len(file_paths)
                logger.info(
                    f"批量上传 [{n}/{total}]：{filenames[i]}")
                with open(fp, 'rb') as f:
                    upload_response = requests.put(
                        upload_url, data=f, timeout=120)
                if upload_response.status_code == 200:
                    upload_success.append(fp)
                    logger.info(f"文件上传成功：{filenames[i]}")
                else:
                    logger.error(
                        f"文件上传失败 [{n}]："
                        f"{upload_response.status_code}")
            except Exception as e:
                logger.error(f"文件上传异常 [{i+1}]：{e}")

        if not upload_success:
            logger.error("所有文件上传均失败")
            return self._batch_fallback_individual(
                file_paths, mode, logger)

        # Step 3: 轮询批次状态并下载全部结果
        all_results = self._poll_batch_all_results(
            batch_id, upload_success)
        if all_results is None:
            return self._batch_fallback_individual(
                file_paths, mode, logger)

        return all_results

    def _batch_fallback_individual(
        self,
        file_paths: list,
        mode: str,
        logger
    ) -> dict:
        """批量上传失败时回退到逐个转换（含三级回退策略）"""
        logger.warning("批量上传失败，回退到逐个文件转换")
        results = {}
        for fp in file_paths:
            content = self.convert_file(fp, mode=mode)
            if content is not None:
                results[fp] = content
        return results

    def _poll_batch_all_results(
        self, batch_id: str, file_paths: list
    ):
        """轮询批量任务状态并下载全部文件的转换结果"""
        logger2 = get_logger()
        logger2.info(
            f"批次 {batch_id} 已提交（{len(file_paths)} 个文件）"
            "，开始轮询...")
        start_time = time.time()
        query_url = (
            f"{self.precision_base_url}"
            f"/api/v4/extract-results/batch/{batch_id}")

        while time.time() - start_time < self.max_poll_time:
            try:
                response = requests.get(
                    query_url, headers=self.headers, timeout=30)
                if response.status_code != 200:
                    logger2.warning(
                        f"查询批次状态失败：{response.status_code}")
                    time.sleep(self.poll_interval)
                    continue

                result = response.json()
                if result.get('code') != 0:
                    msg = result.get('msg', '未知错误')
                    logger2.warning(f"查询批次状态异常：{msg}")
                    time.sleep(self.poll_interval)
                    continue

                batch_data = result.get('data', {})
                extract_results = batch_data.get('extract_result', [])

                if not extract_results:
                    elapsed = int(time.time() - start_time)
                    logger2.debug(
                        f"批次 {batch_id} 处理中...（耗时 {elapsed}s）")
                    time.sleep(self.poll_interval)
                    continue

                all_done = all(
                    r.get('state') in ('done', 'failed')
                    for r in extract_results
                )

                if all_done:
                    logger2.info(f"批次 {batch_id} 全部完成")
                    results = {}
                    for i2, extract_r in enumerate(extract_results):
                        if extract_r.get('state') == 'done':
                            full_zip_url = extract_r.get(
                                'full_zip_url', '')
                            if full_zip_url:
                                md_content = self._download_result(
                                    full_zip_url)
                                if (md_content is not None
                                        and i2 < len(file_paths)):
                                    results[file_paths[i2]] = md_content
                            else:
                                logger2.warning(
                                    f"批次结果 [{i2+1}] 缺少下载链接")
                    return results if results else None

                elapsed = int(time.time() - start_time)
                logger2.debug(
                    f"批次 {batch_id} 处理中...（耗时 {elapsed}s）")

            except requests.RequestException as e:
                logger2.warning(f"轮询请求异常：{e}")

            time.sleep(self.poll_interval)

        logger2.error(
            f"批次 {batch_id} 超时（超过 {self.max_poll_time} 秒）")
        return None


    def _check_agent_limits(self, file_path: str) -> bool:
        """
        检查文件是否满足 Agent 轻量模式的限制

        Agent 模式限制：
        - 文件大小 ≤ 10MB
        - PDF 页数 ≤ 20 页

        Args:
            file_path: 文件路径

        Returns:
            True 表示满足限制，False 表示超限
        """
        logger = get_logger()
        filename = os.path.basename(file_path)

        file_size = os.path.getsize(file_path)
        if file_size > 10 * 1024 * 1024:
            logger.warning(
                f"文件大小 {file_size / 1024 / 1024:.1f}MB 超过 Agent 模式限制（10MB），跳过：{filename}"
            )
            return False

        ext = os.path.splitext(file_path)[1].lower()
        if ext == '.pdf':
            try:
                import pdfplumber
            except ImportError:
                logger.warning("pdfplumber 未安装，无法检测 PDF 页数，继续尝试 Agent 模式")
                return True
            
            try:
                with pdfplumber.open(file_path) as pdf:
                    page_count = len(pdf.pages)
                    if page_count > 20:
                        logger.warning(
                            f"PDF 页数 {page_count} 超过 Agent 模式限制（20 页），跳过：{filename}"
                        )
                        return False
            except Exception as e:
                logger.debug(f"无法检测 PDF 页数，继续尝试 Agent 模式：{e}")

        return True

    def _convert_agent(self, file_path: str) -> Optional[str]:
        """
        轻量模式转换

        使用 Agent Lightweight Extract API，不需要 Token（IP 限流），
        输出为 Markdown CDN 链接。

        步骤：
        1. 预检文件大小和 PDF 页数是否满足 Agent 限制
        2. 提交文件名获取 task_id 和预签名上传 URL
        3. 上传本地文件到预签名 URL
        4. 轮询任务状态直到完成
        5. 下载 Markdown 结果

        注意：agent 模式一次只能解析一个文件

        Args:
            file_path: 文件路径

        Returns:
            Markdown 文本
        """
        logger = get_logger()
        filename = os.path.basename(file_path)

        if not self._check_agent_limits(file_path):
            return None

        submit_url = f"{self.agent_base_url}/api/v1/agent/parse/file"

        # Step 1: 提交文件名获取上传 URL
        try:
            logger.info(f"Agent 模式提交文件：{filename}")
            response = requests.post(
                submit_url,
                json={"file_name": filename},
                timeout=60
            )

            if response.status_code != 200:
                logger.error(f"Agent 提交失败：{response.status_code} {response.text}")
                return None

            result = response.json()
            if result.get('code') != 0:
                logger.error(f"Agent 提交失败：{result.get('msg', '未知错误')}")
                return None

            task_id = result['data']['task_id']
            file_url = result['data'].get('file_url', '')
            logger.info(f"Agent 任务已提交：{task_id}")

        except requests.RequestException as e:
            logger.error(f"Agent 提交异常：{e}")
            return None

        # Step 2: 上传文件到预签名 URL
        if file_url:
            try:
                logger.info(f"上传文件：{filename}")
                with open(file_path, 'rb') as f:
                    upload_response = requests.put(file_url, data=f, timeout=120)

                if upload_response.status_code != 200:
                    logger.error(f"文件上传失败：{upload_response.status_code}")
                    return None

                logger.info(f"文件上传成功：{filename}")

            except requests.RequestException as e:
                logger.error(f"文件上传异常：{e}")
                return None

        # Step 3: 轮询任务状态
        return self._poll_agent_task(task_id)

    def _poll_agent_task(self, task_id: str) -> Optional[str]:
        """
        轮询 Agent 轻量模式的任务状态并获取结果

        Agent 模式返回 Markdown CDN 链接（非 ZIP），
        需要从 CDN 下载 Markdown 内容。

        Args:
            task_id: 任务 ID

        Returns:
            转换后的 Markdown 文本
        """
        logger = get_logger()
        logger.info(f"Agent 任务 {task_id} 已提交，开始轮询状态...")
        start_time = time.time()
        query_url = f"{self.agent_base_url}/api/v1/agent/parse/{task_id}"

        while time.time() - start_time < self.max_poll_time:
            try:
                response = requests.get(query_url, timeout=30)
                if response.status_code != 200:
                    logger.warning(f"查询 Agent 任务状态失败：{response.status_code}")
                    time.sleep(self.poll_interval)
                    continue

                result = response.json()
                if result.get('code') != 0:
                    logger.warning(f"查询 Agent 任务状态异常：{result.get('msg', '未知错误')}")
                    time.sleep(self.poll_interval)
                    continue

                data = result.get('data', {})
                state = data.get('state', '')

                if state == 'done':
                    logger.info(f"Agent 任务 {task_id} 已完成")
                    md_url = data.get('markdown_url', '') or data.get('md_url', '')
                    if md_url:
                        return self._download_md(md_url)
                    logger.warning("Agent 任务完成但未获取到 Markdown 链接")
                    return None

                elif state == 'failed':
                    err_msg = data.get('err_msg', '未知错误')
                    logger.error(f"Agent 任务失败：{err_msg}")
                    return None

                logger.debug(f"Agent 任务 {task_id} 处理中...（状态：{state}，耗时 {int(time.time() - start_time)}s）")

            except requests.RequestException as e:
                logger.warning(f"轮询 Agent 任务异常：{e}")

            time.sleep(self.poll_interval)

        logger.error(f"Agent 任务 {task_id} 超时（超过 {self.max_poll_time} 秒）")
        return None

    def _download_md(self, md_url: str) -> Optional[str]:
        """
        从 CDN 链接下载 Markdown 内容

        Agent 模式的结果以 CDN 链接形式返回，直接下载文本即可。

        Args:
            md_url: Markdown CDN 链接

        Returns:
            Markdown 文本
        """
        logger = get_logger()

        try:
            logger.info(f"下载 Markdown：{md_url}")
            response = requests.get(md_url, timeout=120)
            if response.status_code != 200:
                logger.error(f"下载 Markdown 失败：{response.status_code}")
                return None
            return response.text

        except requests.RequestException as e:
            logger.error(f"下载 Markdown 异常：{e}")
            return None

    def _poll_batch_result(self, batch_id: str) -> Optional[str]:
        """
        轮询批次任务状态并下载结果

        每隔 poll_interval 秒查询一次批次状态，
        直到任务完成或超过 max_poll_time 超时时间。

        Args:
            batch_id: 批次 ID

        Returns:
            转换后的 Markdown 文本
        """
        logger = get_logger()
        logger.info(f"批次 {batch_id} 已提交，开始轮询状态...")
        start_time = time.time()
        query_url = f"{self.precision_base_url}/api/v4/extract-results/batch/{batch_id}"

        while time.time() - start_time < self.max_poll_time:
            try:
                response = requests.get(query_url, headers=self.headers, timeout=30)
                if response.status_code != 200:
                    logger.warning(f"查询批次状态失败：{response.status_code}")
                    time.sleep(self.poll_interval)
                    continue

                result = response.json()
                if result.get('code') != 0:
                    logger.warning(f"查询批次状态异常：{result.get('msg', '未知错误')}")
                    time.sleep(self.poll_interval)
                    continue

                batch_data = result.get('data', {})
                extract_results = batch_data.get('extract_result', [])

                if extract_results:
                    first_result = extract_results[0]
                    state = first_result.get('state', '')

                    if state == 'done':
                        logger.info(f"批次 {batch_id} 已完成")
                        full_zip_url = first_result.get('full_zip_url', '')
                        if full_zip_url:
                            return self._download_result(full_zip_url)
                        logger.warning("批次完成但未获取到结果链接")
                        return None

                    elif state == 'failed':
                        err_msg = first_result.get('err_msg', '未知错误')
                        logger.error(f"文件转换失败：{err_msg}")
                        return None

                    else:
                        logger.debug(f"批次 {batch_id} 处理中...（状态：{state}，耗时 {int(time.time() - start_time)}s）")
                else:
                    logger.debug(f"批次 {batch_id} 处理中...（耗时 {int(time.time() - start_time)}s）")

            except requests.RequestException as e:
                logger.warning(f"轮询请求异常：{e}")

            time.sleep(self.poll_interval)

        logger.error(f"批次 {batch_id} 超时（超过 {self.max_poll_time} 秒）")
        return None

    def _download_result(self, download_url: str) -> Optional[str]:
        """
        从 URL 下载转换结果并提取 Markdown 内容

        结果以 ZIP 压缩包形式提供，解压后查找其中的 .md 文件。

        Args:
            download_url: 结果下载 URL

        Returns:
            提取的 Markdown 文本
        """
        logger = get_logger()

        try:
            logger.info(f"下载转换结果：{download_url}")
            response = requests.get(download_url, timeout=120)
            if response.status_code != 200:
                logger.error(f"下载失败：{response.status_code}")
                return None

            content_type = response.headers.get('Content-Type', '')

            if 'application/zip' in content_type or download_url.endswith('.zip'):
                return self._extract_markdown_from_zip(response.content)
            else:
                return response.text

        except requests.RequestException as e:
            logger.error(f"下载异常：{e}")
            return None

    def _extract_markdown_from_zip(self, zip_content: bytes) -> Optional[str]:
        """
        从 ZIP 压缩包中提取 Markdown 文件内容

        遍历 ZIP 中的所有文件，查找 .md 文件并读取其内容。
        优先查找 full.md（MinerU 完整合并输出），如果不存在则合并所有 .md 文件。

        Args:
            zip_content: ZIP 文件的二进制内容

        Returns:
            合并后的 Markdown 文本
        """
        logger = get_logger()

        try:
            with zipfile.ZipFile(io.BytesIO(zip_content)) as zf:
                md_contents = []
                full_md = None

                for name in zf.namelist():
                    if name.endswith('.md') or name.endswith('.markdown'):
                        content = zf.read(name).decode('utf-8')
                        # 优先使用 full.md（MinerU 的完整 Markdown 输出）
                        if os.path.basename(name) == 'full.md':
                            full_md = content
                        else:
                            md_contents.append(content)

                if full_md:
                    return full_md
                elif md_contents:
                    return '\n\n'.join(md_contents)
                else:
                    logger.warning("ZIP 包中未找到 Markdown 文件")
                    return None

        except zipfile.BadZipFile:
            logger.error("无效的 ZIP 文件")
            return None
        except Exception as e:
            logger.error(f"解压文件异常：{e}")
            return None
