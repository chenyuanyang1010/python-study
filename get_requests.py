import requests
url="https://httpbin.org/get"
params={"format":"json"}
a=requests.get(url,params=params,timeout=10)
try:
   result= a.status_code
   if result!=200:
       print(f"请求失败，状态码{result}")
   else:
       data = a.json()
   print("完整返回：", data)
   print("我们传的params参数：", data["args"])
except Exception as e:
    print("网络异常",e)