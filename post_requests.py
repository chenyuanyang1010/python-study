import requests

def post_demo():
    url = "https://httpbin.org/post"
    headers = {
        "User-Agent": "my-python-study-demo"
    }
    body_data = {
        "username": "chenyuanyang1010",
        "age": 21
    }
    try:
        resp = requests.post(url, json=body_data, headers=headers, timeout=10)
        if resp.status_code != 200:
            print(f"post请求失败，状态码{resp.status_code}")
            return
        res_json = resp.json()
        print("post返回结果：")
        print(res_json)

    except Exception as e:
        print("post网络异常", e)


if __name__ == "__main__":
    post_demo()
