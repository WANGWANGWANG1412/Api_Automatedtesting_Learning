import json

import requests


class RequestsMethod(object):
    # 本项目无请求头

    def get_main(self, url, params):
        response = requests.get(url=url, params=params)
        '''
        if header is not None:
            response = requests.get(url=url, headers=headers, data=data)
        else:
            response = requests.get(url=url, data=data)
        '''
        print("返回数据：", response.text)
        print("状态码：", response.status_code)
        return response

    def post_main(self, url, json):
        response = requests.post(url=url, json=json)
        print("返回数据：", response.text)
        print("状态码：", response.status_code)
        return response

    def put_main(self, url, json):
        response = requests.put(url=url, json=json)
        print("返回数据：", response.text)
        print("状态码：", response.status_code)
        return response

    def delete_main(self, url, data):
        response = requests.delete(url=url, params=data)
        print("返回数据：", response.text)
        print("状态码：", response.status_code)
        return response


if __name__ == '__main__':
    run = RequestsMethod()
    method = "Delete"
    url = "http://127.0.0.1:8099/api/departments/T01/"
    res = run.delete_main(url, None)
    q = json.loads(res.text)
    print(type(q))