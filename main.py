import requests

url = "http://127.0.0.1:8099/api/departments/T001/"
param = None
res = requests.delete(url=url, data=None)
print(res.text)