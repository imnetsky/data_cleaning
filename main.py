"""
文档清洗工具 - 命令行入口

提供一键式文档清洗功能，支持：
1. 直接清洗 Markdown 文件
2. Excel 文件自动转换为 Markdown 后清洗
3. 使用 MinerU API 将 PDF/Word/PPT/图片等转换为 Markdown 后清洗
4. 支持 precision（精准）和 agent（轻量）两种 MinerU 转换模式
5. MinerU 转换三级回退策略：精准模式 → Agent 轻量模式 → 本地转换
6. 带进度显示的多文件批量处理
7. 日志同时输出到控制台和 log/ 目录下的日志文件
"""

import os
import sys
import shutil
import argparse
from tqdm import tqdm

from doc_cleaner import MarkdownCleaner
from doc_cleaner.utils.file_io import (
    read_file,
    write_file,
    list_markdown_files,
    list_excel_files,
    list_non_markdown_files,
)
from doc_cleaner.utils.excel_converter import excel_to_markdown
from doc_cleaner.utils.mineru_client import MinerUClient
from doc_cleaner.utils.config import get_config
from doc_cleaner.utils.logger import setup_logger, get_logger


def main():
    """
    主函数：解析命令行参数，执行文档清洗流程

    命令行参数：
    - input_dir: 输入目录（必需）
    - output_dir: 输出目录（必需）
    - --config: 配置文件路径（可选）
    - --mode: MinerU 转换模式，precision/agent（可选，默认使用 config.yaml 中的配置）
    """
    parser = argparse.ArgumentParser(description='Markdown 文档清洗工具')
    parser.add_argument('input_dir', help='输入目录路径')
    parser.add_argument('output_dir', help='输出目录路径')
    parser.add_argument('--config', default='config.yaml', help='配置文件路径（可选，默认使用 config.yaml）')
    parser.add_argument('--mode', choices=['precision', 'agent'], default=None,
                        help='MinerU 转换模式：precision（精准）/agent（轻量），默认使用配置文件中的设置')
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir
    config_path = args.config

    # Step 1: 验证输入目录
    if not os.path.exists(input_dir):
        print(f"错误：输入目录 {input_dir} 不存在")
        sys.exit(1)

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # Step 2: 初始化日志（在清洗器实例化之前，确保日志目录正确）
    project_root = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(project_root, 'log')
    logger = setup_logger(log_dir=log_dir)

    # Step 3: 初始化清洗器（加载配置文件）
    cleaner = MarkdownCleaner(config_path=config_path)

    # Step 4: 获取配置参数
    config = get_config()
    batch_size = config.get('processing', {}).get('batch_size', 2)

    # MinerU 模式：命令行参数优先，否则使用 config.yaml 中的配置
    mode = args.mode or config['mineru'].get('mode', 'precision')

    # 校验 MinerU 模式合法性
    if mode not in ('precision', 'agent'):
        logger.error(f"无效的 MinerU 模式 '{mode}'，仅支持 'precision' 或 'agent'")
        sys.exit(1)

    logger.info("=" * 60)
    logger.info("文档清洗工具启动")
    logger.info(f"输入目录：{input_dir}")
    logger.info(f"输出目录：{output_dir}")
    logger.info(f"MinerU 模式：{mode}")
    logger.info(f"批次大小：{batch_size}")
    if config_path:
        logger.info(f"配置文件：{config_path}")
    logger.info("=" * 60)

    # 收集所有待处理的 Markdown 文件
    markdown_files = list_markdown_files(input_dir)

    if markdown_files:
        logger.info(f"发现 {len(markdown_files)} 个 Markdown 文件，开始处理...")
        _process_markdown_files(markdown_files, input_dir, output_dir, cleaner, batch_size)
    else:
        logger.info("未发现 Markdown 文件")

    # 收集并处理 Excel 文件
    excel_files = list_excel_files(input_dir)
    if excel_files:
        logger.info(f"发现 {len(excel_files)} 个 Excel 文件，开始转换...")
        _process_excel_files(excel_files, input_dir, output_dir, cleaner, batch_size)

    # 收集并处理需要 MinerU 转换的其他文件
    other_files = list_non_markdown_files(input_dir)
    if other_files:
        fallback_desc = f"{mode} 模式 → Agent 轻量模式 → 本地转换" if mode == 'precision' else f"{mode} 模式 → 本地转换"
        logger.info(f"发现 {len(other_files)} 个非 Markdown 文件，开始转换（回退策略：{fallback_desc}）...")
        _process_mineru_files(other_files, input_dir, output_dir, cleaner, batch_size, mode)

    logger.info("=" * 60)
    logger.info(f"所有文件处理完成！输出目录：{output_dir}")
    logger.info("=" * 60)


def _process_markdown_files(md_files: list, input_dir: str, output_dir: str,
                             cleaner: MarkdownCleaner, batch_size: int) -> None:
    """
    批量处理 Markdown 文件：直接读取内容后清洗

    按 batch_size 分批处理，避免同时占用过多资源。

    Args:
        md_files: Markdown 文件路径列表
        input_dir: 输入目录（用于计算相对路径）
        output_dir: 输出目录
        cleaner: Markdown 清洗器实例
        batch_size: 每批处理的文件数
    """
    logger = get_logger()
    total = len(md_files)
    processed = 0

    with tqdm(total=total, desc="清洗 Markdown 文件", unit="个") as pbar:
        for batch_start in range(0, total, batch_size):
            batch_end = min(batch_start + batch_size, total)
            batch = md_files[batch_start:batch_end]
            logger.info(f"处理第 {batch_start + 1}-{batch_end} 个文件（批次大小：{batch_size}）")

            for md_file in batch:
                try:
                    logger.info(f"读取文件：{md_file}")
                    content = read_file(md_file)

                    logger.info(f"开始清洗：{md_file}")
                    cleaned = cleaner.clean(content)

                    rel_path = os.path.relpath(md_file, input_dir)
                    output_path = os.path.join(output_dir, rel_path)

                    write_file(cleaned, output_path)
                    processed += 1
                    logger.info(f"完成：{rel_path}")

                except Exception as e:
                    logger.error(f"处理文件 {md_file} 失败：{e}")

                pbar.update(1)

    logger.info(f"Markdown 文件处理完成：{processed}/{total} 个成功")


def _process_excel_files(excel_files: list, input_dir: str, output_dir: str,
                          cleaner: MarkdownCleaner, batch_size: int) -> None:
    """
    批量处理 Excel 文件：先转为 Markdown 表格，再清洗

    使用基础清洗模式（clean_basic），因为 Excel 数据表格不需要 LLM 分析。
    按 batch_size 分批处理。

    Args:
        excel_files: Excel 文件路径列表
        input_dir: 输入目录（用于计算相对路径）
        output_dir: 输出目录
        cleaner: Markdown 清洗器实例
        batch_size: 每批处理的文件数
    """
    logger = get_logger()
    total = len(excel_files)
    processed = 0

    with tqdm(total=total, desc="转换 Excel 文件", unit="个") as pbar:
        for batch_start in range(0, total, batch_size):
            batch_end = min(batch_start + batch_size, total)
            batch = excel_files[batch_start:batch_end]
            logger.info(f"处理第 {batch_start + 1}-{batch_end} 个 Excel 文件")

            for excel_file in batch:
                try:
                    logger.info(f"转换 Excel：{excel_file}")
                    markdown_content = excel_to_markdown(excel_file)
                    if markdown_content is None:
                        logger.warning(f"跳过文件 {excel_file}（转换失败）")
                        pbar.update(1)
                        continue

                    logger.info(f"开始清洗：{excel_file}")
                    cleaned = cleaner.clean_basic(markdown_content)

                    rel_path = os.path.relpath(excel_file, input_dir)
                    output_rel_path = os.path.splitext(rel_path)[0] + '.md'
                    output_path = os.path.join(output_dir, output_rel_path)

                    write_file(cleaned, output_path)
                    processed += 1
                    logger.info(f"完成：{rel_path} -> {output_rel_path}")

                except Exception as e:
                    logger.error(f"处理文件 {excel_file} 失败：{e}")

                pbar.update(1)

    logger.info(f"Excel 文件处理完成：{processed}/{total} 个成功")


def _process_mineru_files(other_files: list, input_dir: str, output_dir: str,
                           cleaner: MarkdownCleaner, batch_size: int, mode: str) -> None:
    """
    批量通过 MinerU API 转换并清洗文件

    先用 MinerU 将非 Markdown 文件（PDF/Word/PPT/图片等）转换为 Markdown，
    再对转换结果进行清洗。

    MinerU 转换采用三级回退策略：
    1. 使用指定模式调用 MinerU API
    2. 如果 precision 模式失败，自动尝试 agent 轻量模式
    3. 如果所有 MinerU 模式均失败，回退到本地转换（需配置 fallback_local_convert: true）

    特别注意：
    - agent（轻量）模式一次只能解析一个文件，因此强制 batch_size=1
    - precision（精准）模式支持批量处理，按配置的 batch_size 分批

    Args:
        other_files: 待转换的文件路径列表
        input_dir: 输入目录（用于计算相对路径）
        output_dir: 输出目录
        cleaner: Markdown 清洗器实例
        batch_size: 每批处理的文件数
        mode: MinerU 转换模式
    """
    logger = get_logger()

    # agent 模式一次只能解析一个文件
    if mode == 'agent':
        logger.info("agent（轻量）模式：一次只能解析一个文件，强制批次大小为 1")
        effective_batch_size = 1
    else:
        effective_batch_size = batch_size

    temp_dir = os.path.join(output_dir, '.temp_mineru')
    os.makedirs(temp_dir, exist_ok=True)

    mineru_client = MinerUClient()

    total = len(other_files)
    processed_count = 0

    tqdm_desc = f"MinerU {mode}" + ("→agent→local" if mode == 'precision' else "→local")
    with tqdm(total=total, desc=tqdm_desc, unit="个") as pbar:
        for batch_start in range(0, total, effective_batch_size):
            batch_end = min(batch_start + effective_batch_size, total)
            batch = other_files[batch_start:batch_end]
            logger.info(f"MinerU 处理第 {batch_start + 1}-{batch_end} 个文件（模式：{mode}）")

            if mode == 'precision' and len(batch) > 1:
                # 真正的批量上传：一次 API 调用提交整个批次
                batch_results = mineru_client.convert_files_batch(batch, mode=mode)
                for other_file in batch:
                    try:
                        result = batch_results.get(other_file)
                        if result is None:
                            logger.warning(f"文件 {other_file} 转换失败，跳过")
                            pbar.update(1)
                            continue

                        logger.info(f"清洗转换结果：{other_file}")
                        cleaned = cleaner.clean(result)

                        temp_md_path = os.path.join(temp_dir, os.path.basename(other_file) + '.md')
                        write_file(cleaned, temp_md_path)

                        rel_path = os.path.relpath(other_file, input_dir)
                        output_rel_path = os.path.splitext(rel_path)[0] + '.md'
                        output_path = os.path.join(output_dir, output_rel_path)
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                        shutil.copy2(temp_md_path, output_path)

                        processed_count += 1
                        logger.info(f"完成：{rel_path} -> {output_rel_path}")

                    except Exception as e:
                        logger.error(f"处理文件 {other_file} 失败：{e}")

                    pbar.update(1)
            else:
                for other_file in batch:
                    try:
                        logger.info(f"上传文件进行 {mode} 模式转换：{other_file}")
                        result = mineru_client.convert_file(other_file, mode=mode)
                        if result is None:
                            logger.warning(f"文件 {other_file} 转换失败，跳过")
                            pbar.update(1)
                            continue

                        logger.info(f"清洗转换结果：{other_file}")
                        cleaned = cleaner.clean(result)

                        temp_md_path = os.path.join(temp_dir, os.path.basename(other_file) + '.md')
                        write_file(cleaned, temp_md_path)

                        rel_path = os.path.relpath(other_file, input_dir)
                        output_rel_path = os.path.splitext(rel_path)[0] + '.md'
                        output_path = os.path.join(output_dir, output_rel_path)
                        os.makedirs(os.path.dirname(output_path), exist_ok=True)
                        shutil.copy2(temp_md_path, output_path)

                        processed_count += 1
                        logger.info(f"完成：{rel_path} -> {output_rel_path}")

                    except Exception as e:
                        logger.error(f"处理文件 {other_file} 失败：{e}")

                    pbar.update(1)

    try:
        shutil.rmtree(temp_dir, ignore_errors=True)
    except Exception:
        pass

    logger.info(f"MinerU 转换完成：{processed_count}/{total} 个成功")


if __name__ == '__main__':
    main()
