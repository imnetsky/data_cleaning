import requests
import os
import time
import json

API_KEY = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI3NDkwOTQ2OSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTc3NTcxMDA1OSwiY2xpZW50SWQiOiJsa3pkeDU3bnZ5MjJqa3BxOXgydyIsInBob25lIjoiMTM5NzEyNTA5NzEiLCJvcGVuSWQiOm51bGwsInV1aWQiOiI3YjdjMDI3YS05NzQ3LTQ5ZGItYWFmNC1jMzhmNjUzOTZhYmUiLCJlbWFpbCI6IiIsImV4cCI6MTc4MzQ4NjA1OX0.XOnNC3ItLyQO2XWFRoxGgZlNT3NlcqWtCIlt4EYvi_nx0WzbJU85bYRzudjqFVGg8-kJMYWGLlArohtnA97tuA"
BASE_URL = "https://mineru.net/api/v4"

def get_upload_urls(file_names, model_version="vlm"):
    print(f"[获取上传URL] 请求URL: {BASE_URL}/file-urls/batch")
    print(f"[获取上传URL] 请求文件数量: {len(file_names)}")

    url = f"{BASE_URL}/file-urls/batch"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    files_data = [{"name": name, "data_id": f"file_{i}"} for i, name in enumerate(file_names)]

    data = {
        "files": files_data,
        "model_version": model_version
    }

    response = requests.post(url, headers=headers, json=data)

    print(f"[获取上传URL] 响应状态码: {response.status_code}")

    if response.status_code == 200:
        result = response.json()
        print(f"[获取上传URL] 响应结果: code={result.get('code')}, msg={result.get('msg')}")
        return result
    else:
        print(f"[获取上传URL] 失败: {response.status_code} - {response.text}")
        return None

def upload_file(upload_url, file_path):
    print(f"[上传文件] 正在上传: {os.path.basename(file_path)}")

    with open(file_path, "rb") as f:
        response = requests.put(upload_url, data=f)

    if response.status_code == 200:
        print(f"[上传文件] 成功: {os.path.basename(file_path)}")
        return True
    else:
        print(f"[上传文件] 失败: {response.status_code}")
        return False

def get_batch_result(batch_id):
    url = f"{BASE_URL}/extract-results/batch/{batch_id}"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"[查询批量任务] 失败: {response.status_code}")
        return None

def download_zip(url, save_path):
    print(f"[下载结果] 正在下载: {url}")
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"[下载结果] 已保存到: {save_path}")
        return True
    else:
        print(f"[下载结果] 失败: {response.status_code}")
        return False

def main():
    print("=" * 60)
    print("MinerU 本地文件批量上传解析测试")
    print("=" * 60)

    docx_files = [
        "协同办公系统卡顿现象分析报告-2023年2月10日.docx",
        "生产事件复盘报告-（IN20230220000026）优理宝移动终端浙江区域少量客户登录异常(1).docx",
        "生产事件复盘报告-（IN20240729000016）同余数据报送异常.docx"
    ]

    file_paths = []
    for f in docx_files:
        path = os.path.join(os.getcwd(), f)
        if os.path.exists(path):
            file_paths.append(path)
            print(f"[找到文件] {f} ({os.path.getsize(path)} bytes)")
        else:
            print(f"[未找到] {f}")

    if not file_paths:
        print("[错误] 没有找到任何文件")
        return

    print(f"\n[开始] 待处理文件数量: {len(file_paths)}")

    print("\n" + "-" * 60)
    print("步骤1: 批量申请上传URL")
    print("-" * 60)

    result = get_upload_urls(docx_files, model_version="vlm")
    if not result or result.get("code") != 0:
        print("[错误] 获取上传URL失败")
        return

    batch_id = result["data"]["batch_id"]
    upload_urls = result["data"]["file_urls"]

    print(f"[成功] batch_id: {batch_id}")
    print(f"[成功] 获取到 {len(upload_urls)} 个上传URL")

    print("\n" + "-" * 60)
    print("步骤2: 上传本地文件到OSS")
    print("-" * 60)

    for i, file_path in enumerate(file_paths):
        if i < len(upload_urls):
            success = upload_file(upload_urls[i], file_path)
            if not success:
                print(f"[错误] 文件上传失败: {docx_files[i]}")
        time.sleep(1)

    print("\n" + "-" * 60)
    print("步骤3: 等待系统自动创建解析任务")
    print("-" * 60)

    print(f"[提示] 超时时间: 300秒")
    print("")

    start_time = time.time()
    timeout = 300

    while True:
        elapsed = time.time() - start_time
        current_time = time.strftime("%H:%M:%S", time.localtime())

        if elapsed >= timeout:
            print(f"[{current_time}] 超时！等待时间已超过 {timeout} 秒")
            return

        print(f"[{current_time}] 轮询中... ({int(elapsed)}s/{timeout}s)")

        batch_result = get_batch_result(batch_id)

        if batch_result and batch_result.get("code") == 0:
            extract_results = batch_result["data"].get("extract_result", [])

            if extract_results:
                all_done = True
                any_failed = False

                for idx, result_item in enumerate(extract_results):
                    file_name = result_item.get("file_name", "未知")
                    state = result_item.get("state", "unknown")
                    full_zip_url = result_item.get("full_zip_url", "")

                    if state == "done":
                        print(f"[{current_time}] 文件{idx+1}: {file_name} -> 完成")
                        if full_zip_url:
                            zip_name = f"parse_result_{idx+1}.zip"
                            zip_path = os.path.join(os.getcwd(), zip_name)
                            download_zip(full_zip_url, zip_path)
                    elif state == "failed":
                        err_msg = result_item.get("err_msg", "未知错误")
                        print(f"[{current_time}] 文件{idx+1}: {file_name} -> 失败: {err_msg}")
                        any_failed = True
                    elif state == "running":
                        print(f"[{current_time}] 文件{idx+1}: {file_name} -> 处理中...")
                        all_done = False
                    elif state == "waiting-file":
                        print(f"[{current_time}] 文件{idx+1}: {file_name} -> 等待文件...")
                        all_done = False
                    else:
                        print(f"[{current_time}] 文件{idx+1}: {file_name} -> {state}")
                        all_done = False

                if all_done and not any_failed:
                    result_data = {
                        "batch_id": batch_id,
                        "results": extract_results
                    }
                    result_file = "parse_results.json"
                    with open(result_file, "w", encoding="utf-8") as f:
                        json.dump(result_data, f, ensure_ascii=False, indent=2)
                    print(f"\n[完成] 所有文件解析完成，结果已保存到: {result_file}")
                    break

                if any_failed:
                    print("\n[错误] 部分文件解析失败")
                    break
            else:
                print(f"[{current_time}] 等待系统创建任务...")
        else:
            print(f"[{current_time}] 等待系统响应...")

        time.sleep(5)

    print("\n" + "=" * 60)
    print("测试完成")
    print("=" * 60)

if __name__ == "__main__":
    main()