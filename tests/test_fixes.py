"""
修复验证测试 - 验证代码与需求一致性分析报告中的问题修复

测试项：
1. Q2: local_converter.py 中 Table 类导入问题
2. Q3: local_converter.py 中 _escape_markdown 过度转义
3. Q1: local_converter.py 和 docx_converter.py 重复代码
4. M1: DenoiseProcessor 页眉页脚检测
5. D2: LLM 文档概要 200 字符硬性截断
6. D3: __version__ 版本号一致性
7. D4/D5: config.py 与 config.yaml 默认值一致性
"""

import sys
import os
import re

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将项目根目录添加到 Python 路径
sys.path.insert(0, PROJECT_ROOT)


def _read_file(relative_path):
    """读取项目文件内容"""
    file_path = os.path.join(PROJECT_ROOT, relative_path)
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def test_q2_local_converter_table_import():
    """Q2: 验证 local_converter.py 不再直接使用未导入的 Table 类"""
    source = _read_file('doc_cleaner/utils/local_converter.py')
    assert 'Table(element' not in source, "Q2 修复失败：仍存在未导入的 Table 使用"
    assert 'docx_converter' in source, "Q2 修复失败：未复用 docx_converter 模块"
    print("  [PASS] Q2: local_converter.py Table 导入问题已修复")


def test_q3_escape_markdown():
    """Q3: 验证 local_converter.py 中不再有 _escape_markdown 过度转义问题"""
    source = _read_file('doc_cleaner/utils/local_converter.py')

    # _escape_markdown 函数已随 Excel 转换代码一起移除
    assert '_escape_markdown' not in source, \
        "Q3 修复失败：local_converter 仍包含 _escape_markdown 函数"

    # Excel 转换已移至 excel_converter 模块，由 main.py 单独处理
    assert '_convert_excel_to_markdown' not in source, \
        "Q3 修复失败：local_converter 仍包含 Excel 转换代码"

    print("  [PASS] Q3: _escape_markdown 过度转义问题已修复（函数已移除）")


def test_q1_no_duplicate_docx_code():
    """Q1: 验证 local_converter 不再包含重复的 DOCX 转换代码"""
    source = _read_file('doc_cleaner/utils/local_converter.py')

    assert '_parse_docx_paragraph' not in source, \
        "Q1 修复失败：local_converter 仍包含 _parse_docx_paragraph"
    assert '_parse_docx_table' not in source, \
        "Q1 修复失败：local_converter 仍包含 _parse_docx_table"

    print("  [PASS] Q1: local_converter 和 docx_converter 重复代码已消除")


def test_m1_repeated_header_footer_removal():
    """M1: 验证 DenoiseProcessor 能移除重复出现的页眉页脚"""
    from doc_cleaner.processors.denoise import DenoiseProcessor

    processor = DenoiseProcessor()

    # 构造包含重复页眉的文档
    content = """# 第一章

公司机密文件
这是正文内容第一段。

公司机密文件
这是正文内容第二段。

公司机密文件
这是正文内容第三段。

公司机密文件
这是正文内容第四段。"""

    result = processor.process(content)

    # 重复出现的页眉行应被移除
    assert result.count('公司机密文件') == 0, \
        f"M1 修复失败：重复页眉未被移除，出现 {result.count('公司机密文件')} 次"

    # 正文内容应保留
    assert '这是正文内容第一段' in result, "正文内容被误删"
    assert '这是正文内容第二段' in result, "正文内容被误删"
    assert '# 第一章' in result, "标题被误删"

    print("  [PASS] M1: 页眉页脚检测功能已增强")


def test_m1_header_footer_not_delete_titles():
    """M1: 验证重复出现的标题不会被误删"""
    from doc_cleaner.processors.denoise import DenoiseProcessor

    processor = DenoiseProcessor()

    content = """# 概述

内容1

# 概述

内容2

# 概述

内容3"""

    result = processor.process(content)
    assert result.count('# 概述') == 3, \
        f"M1 修复失败：重复标题被误删，仅剩 {result.count('# 概述')} 次"

    print("  [PASS] M1: 重复标题不被误删")


def test_m1_chinese_page_number():
    """M1: 验证中文页码格式被识别"""
    from doc_cleaner.processors.denoise import DenoiseProcessor

    processor = DenoiseProcessor()

    content = """正文第一段

第 1 页

正文第二段

第 2 页

正文第三段"""

    result = processor.process(content)
    assert '第 1 页' not in result, "中文页码格式未被移除"
    assert '第 2 页' not in result, "中文页码格式未被移除"
    assert '正文第一段' in result, "正文被误删"

    print("  [PASS] M1: 中文页码格式识别正常")


def test_d2_summary_truncation():
    """D2: 验证 LLM 文档概要和章节摘要的硬性截断"""
    source = _read_file('doc_cleaner/utils/llm_client.py')

    # 验证 summarize_document 包含 200 字符截断逻辑
    assert '200' in source and '截断' in source, \
        "D2 修复失败：summarize_document 缺少 200 字符截断逻辑"

    # 验证 summarize_section 包含 50 字符截断逻辑
    assert '50' in source, \
        "D2 修复失败：summarize_section 缺少 50 字符截断逻辑"

    # 验证截断位置正确（197 + '...' = 200, 47 + '...' = 50）
    assert '197' in source, "D2 修复失败：文档概要截断位置不正确"
    assert '47' in source, "D2 修复失败：章节摘要截断位置不正确"

    print("  [PASS] D2: LLM 摘要硬性截断已添加")


def test_d3_version_consistency():
    """D3: 验证 __version__ 与 README 版本号一致"""
    init_source = _read_file('doc_cleaner/__init__.py')

    # 提取版本号
    version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', init_source)
    assert version_match, "D3 修复失败：找不到 __version__ 定义"

    version = version_match.group(1)
    assert version == '0.3.0', f"D3 修复失败：版本号为 {version}，期望 0.3.0"

    # 验证 README 中包含该版本号
    readme_source = _read_file('README.md')
    assert version in readme_source or f'V{version}' in readme_source, \
        f"D3 修复失败：README 中未找到版本号 {version}"

    print("  [PASS] D3: 版本号已统一为 0.3.0")


def test_d4_d5_config_defaults():
    """D4/D5: 验证 config.py 默认值与 config.yaml 一致"""
    config_source = _read_file('doc_cleaner/utils/config.py')

    # 提取 poll_interval 默认值
    poll_interval_match = re.search(r"'poll_interval'\s*:\s*(\d+)", config_source)
    assert poll_interval_match, "D4 修复失败：找不到 poll_interval 定义"
    poll_interval = int(poll_interval_match.group(1))
    assert poll_interval == 15, \
        f"D4 修复失败：poll_interval 为 {poll_interval}，期望 15"

    # 提取 poll_timeout 默认值
    poll_timeout_match = re.search(r"'poll_timeout'\s*:\s*(\d+)", config_source)
    assert poll_timeout_match, "D5 修复失败：找不到 poll_timeout 定义"
    poll_timeout = int(poll_timeout_match.group(1))
    assert poll_timeout == 300, \
        f"D5 修复失败：poll_timeout 为 {poll_timeout}，期望 300"

    # 验证与 config.yaml 一致
    yaml_source = _read_file('config.yaml')
    yaml_interval_match = re.search(r'poll_interval\s*:\s*(\d+)', yaml_source)
    yaml_timeout_match = re.search(r'poll_timeout\s*:\s*(\d+)', yaml_source)

    if yaml_interval_match:
        yaml_interval = int(yaml_interval_match.group(1))
        assert poll_interval == yaml_interval, \
            f"D4 修复失败：config.py({poll_interval}) != config.yaml({yaml_interval})"

    if yaml_timeout_match:
        yaml_timeout = int(yaml_timeout_match.group(1))
        assert poll_timeout == yaml_timeout, \
            f"D5 修复失败：config.py({poll_timeout}) != config.yaml({yaml_timeout})"

    print("  [PASS] D4/D5: config.py 默认值与 config.yaml 已统一")


def test_new1_config_temperature_max_tokens():
    """#1/#2: 验证 config.yaml 中 temperature 和 max_tokens 与需求一致"""
    yaml_source = _read_file('config.yaml')

    temp_match = re.search(r'temperature\s*:\s*([\d.]+)', yaml_source)
    assert temp_match, "#1 修复失败：config.yaml 中找不到 temperature"
    temp = float(temp_match.group(1))
    assert temp == 0.3, f"#1 修复失败：temperature 为 {temp}，期望 0.3"

    tokens_match = re.search(r'max_tokens\s*:\s*(\d+)', yaml_source)
    assert tokens_match, "#2 修复失败：config.yaml 中找不到 max_tokens"
    tokens = int(tokens_match.group(1))
    assert tokens == 8192, f"#2 修复失败：max_tokens 为 {tokens}，期望 8192"

    print("  [PASS] #1/#2: config.yaml temperature/max_tokens 已修复")


def test_new3_denoise_hr_and_bold():
    """#3: 验证 _is_likely_header_footer 排除水平线变体和加粗文本"""
    from doc_cleaner.processors.denoise import DenoiseProcessor

    processor = DenoiseProcessor()

    # 测试水平线变体不被误删
    content = """# 标题

---

正文1

- - -

正文2

* * *

正文3"""

    result = processor.process(content)
    assert '---' in result, "水平线 --- 被误删"
    assert '- - -' in result, "水平线变体 - - - 被误删"
    assert '* * *' in result, "水平线变体 * * * 被误删"

    # 测试加粗文本不被误删
    content2 = """# 标题

**重要提示**

正文1

**重要提示**

正文2

**重要提示**

正文3"""
    result2 = processor.process(content2)
    assert result2.count('**重要提示**') == 3, \
        f"加粗文本被误删为 {result2.count('**重要提示**')} 次，期望 3 次"

    print("  [PASS] #3: 水平线变体和加粗文本不被误删")


def test_new4_denoise_no_duplicate_newline():
    """#4: 验证 DenoiseProcessor 不再重复统一换行符"""
    source = _read_file('doc_cleaner/processors/denoise.py')

    # 确认 process 方法中不再有换行符统一逻辑
    process_match = re.search(
        r'def process\(self.*?\n(?=\n    def |\nclass |\Z)',
        source, re.DOTALL
    )
    assert process_match, "#4 修复失败：找不到 process 方法"
    process_code = process_match.group(0)
    assert "replace('\\r\\n'" not in process_code, \
        "#4 修复失败：process 方法中仍包含换行符统一逻辑"

    print("  [PASS] #4: DenoiseProcessor 不再重复统一换行符")


def test_new5_unique_placeholders():
    """#5: 验证三个处理器的占位符文本互不冲突"""
    denoise_src = _read_file('doc_cleaner/processors/denoise.py')
    encoding_src = _read_file('doc_cleaner/processors/encoding.py')
    dedup_src = _read_file('doc_cleaner/processors/dedup.py')

    # 验证占位符包含处理器标识
    assert 'DENOISE' in denoise_src and '__DENOISE_CODE_b2e1_' in denoise_src, \
        "#5 修复失败：denoise 占位符缺少处理器标识"
    assert 'ENC' in encoding_src and '__ENC_PUNCT_7f3a_' in encoding_src, \
        "#5 修复失败：encoding 占位符缺少处理器标识"
    assert 'DEDUP' in dedup_src and '__DEDUP_CODE_c4f7_' in dedup_src, \
        "#5 修复失败：dedup 占位符缺少处理器标识"

    print("  [PASS] #5: 三个处理器占位符已唯一化")


def test_new7_context_block_cleanup():
    """#7: 验证 _clean_old_context_blocks 清理逻辑"""
    from doc_cleaner.processors.segment_intro import SegmentIntroProcessor

    processor = SegmentIntroProcessor()

    # 测试标准上下文块被正确清理
    content = """# 第一章

---
文档概要：这是概要
本段概要：这是摘要
逻辑关联：这是关联
---

正文内容"""

    result = processor._clean_old_context_blocks(content)
    assert '文档概要：这是概要' not in result, "上下文块未被清理"
    assert '本段概要：这是摘要' not in result, "上下文块未被清理"
    assert '正文内容' in result, "正文被误删"

    # 测试非上下文块的 --- 不被误删
    content2 = """# 标题

---

普通水平线下方内容"""

    result2 = processor._clean_old_context_blocks(content2)
    assert '---' in result2, "非上下文块的 --- 被误删"
    assert '普通水平线下方内容' in result2, "水平线下方内容被误删"

    print("  [PASS] #7: 上下文块清理逻辑已修复")


def test_new8_mineru_poll_defaults():
    """#8: 验证 MinerUClient 回退默认值与 config.yaml 一致"""
    source = _read_file('doc_cleaner/utils/mineru_client.py')

    interval_match = re.search(r"poll_interval.*?get\('poll_interval',\s*(\d+)\)", source)
    assert interval_match, "#8 修复失败：找不到 poll_interval 回退默认值"
    interval = int(interval_match.group(1))
    assert interval == 15, f"#8 修复失败：poll_interval 回退值为 {interval}，期望 15"

    timeout_match = re.search(r"get\('poll_timeout',\s*(\d+)\)", source)
    assert timeout_match, "#8 修复失败：找不到 poll_timeout 回退默认值"
    timeout = int(timeout_match.group(1))
    assert timeout == 300, f"#8 修复失败：poll_timeout 回退值为 {timeout}，期望 300"

    print("  [PASS] #8: MinerUClient 回退默认值已统一")


def test_new10_hr_boundary_detection():
    """#10: 验证 FormatStandardizationProcessor 水平线边界检测"""
    from doc_cleaner.processors.format_standardization import FormatStandardizationProcessor

    processor = FormatStandardizationProcessor()

    # 测试上下文块中的 --- 不被添加空行
    content = """# 标题
---
文档概要：概要内容
本段概要：摘要内容
---

正文"""
    result = processor._standardize_horizontal_rules(content)
    # 上下文块的 --- 不应在前后被添加额外空行
    lines = result.split('\n')
    # 找到第一个 --- 的位置
    hr_indices = [i for i, l in enumerate(lines) if l.strip() == '---']
    assert len(hr_indices) >= 1, "找不到水平线"

    # 第一个 --- 前面应该是标题行，不应有空行
    first_hr = hr_indices[0]
    if first_hr > 0:
        assert lines[first_hr - 1].strip() == '# 标题', \
            "上下文块 --- 前面被错误插入了空行"

    print("  [PASS] #10: 水平线边界检测已修复")


def test_new11_local_converter_no_excel():
    """#11: 验证 local_converter 不再包含 Excel 转换"""
    source = _read_file('doc_cleaner/utils/local_converter.py')

    assert '_convert_excel_to_markdown' not in source, \
        "#11 修复失败：local_converter 仍包含 Excel 转换函数"
    assert '_parse_excel_sheet' not in source, \
        "#11 修复失败：local_converter 仍包含 Excel 解析函数"

    # 验证 convert_file_to_markdown 不再处理 xlsx/xls
    assert "'.xlsx'" not in source and "'.xls'" not in source, \
        "#11 修复失败：convert_file_to_markdown 仍处理 Excel 扩展名"

    print("  [PASS] #11: local_converter 已移除 Excel 转换")


def test_new12_doc_format_handling():
    """#12: 验证 .doc 格式正确处理"""
    source = _read_file('doc_cleaner/utils/local_converter.py')

    # 验证 .doc 被识别但返回 None
    assert "'.doc'" in source, "#12 修复失败：未处理 .doc 格式"

    # 验证 MinerU 回退路径不包含 .doc
    mineru_src = _read_file('doc_cleaner/utils/mineru_client.py')
    supported_match = re.search(r"supported_extensions\s*=\s*\(([^)]+)\)", mineru_src)
    assert supported_match, "#12 修复失败：找不到 supported_extensions"
    supported = supported_match.group(1)
    assert "'.doc'" not in supported, "#12 修复失败：MinerU 回退路径仍包含 .doc"

    print("  [PASS] #12: .doc 格式处理已修复")


def run_all_tests():
    """运行所有验证测试"""
    tests = [
        ("Q2: local_converter Table 导入问题", test_q2_local_converter_table_import),
        ("Q3: _escape_markdown 过度转义", test_q3_escape_markdown),
        ("Q1: DOCX 重复代码消除", test_q1_no_duplicate_docx_code),
        ("M1: 页眉页脚检测增强", test_m1_repeated_header_footer_removal),
        ("M1: 重复标题不被误删", test_m1_header_footer_not_delete_titles),
        ("M1: 中文页码格式", test_m1_chinese_page_number),
        ("D2: LLM 摘要截断", test_d2_summary_truncation),
        ("D3: 版本号一致性", test_d3_version_consistency),
        ("D4/D5: 配置默认值一致性", test_d4_d5_config_defaults),
        ("#1/#2: config.yaml temperature/max_tokens", test_new1_config_temperature_max_tokens),
        ("#3: 水平线变体和加粗文本排除", test_new3_denoise_hr_and_bold),
        ("#4: DenoiseProcessor 不重复统一换行符", test_new4_denoise_no_duplicate_newline),
        ("#5: 处理器占位符唯一化", test_new5_unique_placeholders),
        ("#7: 上下文块清理逻辑", test_new7_context_block_cleanup),
        ("#8: MinerUClient 回退默认值", test_new8_mineru_poll_defaults),
        ("#10: 水平线边界检测", test_new10_hr_boundary_detection),
        ("#11: local_converter 移除 Excel 转换", test_new11_local_converter_no_excel),
        ("#12: .doc 格式处理", test_new12_doc_format_handling),
    ]

    print("=" * 60)
    print("修复验证测试")
    print("=" * 60)

    passed = 0
    failed = 0
    errors = []

    for name, test_func in tests:
        print(f"\n[测试] {name}")
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"  [FAIL] {e}")
            errors.append((name, str(e)))
            failed += 1
        except Exception as e:
            print(f"  [ERROR] {type(e).__name__}: {e}")
            errors.append((name, f"{type(e).__name__}: {e}"))
            failed += 1

    print("\n" + "=" * 60)
    print(f"测试结果：通过 {passed}/{passed + failed}，失败 {failed}")
    if errors:
        print("\n失败详情：")
        for name, err in errors:
            print(f"  - {name}: {err}")
    print("=" * 60)

    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
