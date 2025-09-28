import requests

# 定义API端点和测试数据
url = "http://localhost:8000/analyze"
problem_description = "test"
code_zip_path = "Cclears.zip"  # 替换为你的测试代码ZIP文件路径

# 发送POST请求
files = {"code_zip": open(code_zip_path, "rb")}
data = {"problem_description": problem_description}

response = requests.post(url, files=files, data=data)

# 打印响应结果
print("Status Code:", response.status_code)
print("Response JSON:", response.json())