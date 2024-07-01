import os
import sys
import time
import http.client
from urllib.parse import urlparse

# 定义PIP源
pip_sources = {
    "1": ("清华大学", "https://pypi.tuna.tsinghua.edu.cn/simple/"),
    "2": ("中国科技大学", "https://pypi.mirrors.ustc.edu.cn/simple/"),
    "3": ("华为云", "https://repo.huaweicloud.com/artifactory/pypi-public/simple/"),
    "4": ("腾讯云", "https://mirrors.cloud.tencent.com/pypi/simple/"),
    "5": ("阿里云", "https://mirrors.aliyun.com/pypi/simple/"),
    "6": ("Pip官方源", "https://pypi.python.org/simple/"),
}

def check_connectivity(url):
    parsed_url = urlparse(url)
    connection = http.client.HTTPSConnection(parsed_url.netloc, timeout=5)
    try:
        start_time = time.time()
        connection.request("HEAD", parsed_url.path)
        response = connection.getresponse()
        latency = (time.time() - start_time) * 1000  # 转换为毫秒
        return response.status == 200, latency
    except Exception as e:
        print(f"调试信息: 无法连接到 {url}。错误: {e}")
        return False, None
    finally:
        connection.close()

def list_sources():
    print("\n{Python Pip Repository Manager}")
    print(f"\n目前可用的 Python Pip 源服务：\n")
    for key, (name, url) in pip_sources.items():
        is_connected, latency = check_connectivity(url)
        # status = "可连接" if is_connected else "不可连接"
        latency_info = f"{latency:.2f} ms" if latency is not None else "N/A"
        print(f"{key}. {name}: {url} (延迟: {latency_info})")

def switch_source(choice):
    if choice in pip_sources:
        name, url = pip_sources[choice]
        os.system(f"pip config set global.index-url {url}")
        print(f"已切换 Python Pip源到 {name} ({url})")
    else:
        print(f"无效的选择，请重新输入。")

def main():
    list_sources()
    while True:
        choice = input(f"\n请选择一个 Python Pip 源 (输入序号): ")
        if choice in pip_sources:
            switch_source(choice)
            break
        else:
            print(f"无效的选择，请输入有效的序号。")

if __name__ == "__main__":
    main()
