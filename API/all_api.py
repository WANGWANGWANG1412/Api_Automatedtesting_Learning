import sys
from UseRequests.run_method import RequestsMethod
from common.read_info import ReadYaml
import json

# 封装所有方法

'''
    1、获取并储存token（此练习项目暂时没用到登录，待实现）
    2、请求模块
    3、接口参数读取模块
    4、日志模块（待实现）
    5、异常处理捕获模块（待实现）
'''


class AllApi(object):
    def __init__(self):
        self.run = RequestsMethod()
        self.read = ReadYaml()

    # 登录，获取token
    '''
    def login(self, api_name):
        XXXXXXX
        XXXXXXX
    '''

    # 接口请求封装
    def send_request(self, api_name):

        # 获取接口请求参数
        method = self.read.get_method(api_name)
        url = self.read.get_url(api_name)
        data = self.read.get_data(api_name)

        # 区分请求方法种类
        if method == "Get":
            response = self.run.get_main(url, data)
            return response
        elif method == "Post":
            response = self.run.post_main(url, data)
            return response
        elif method == "Delete":
            response = self.run.delete_main(url, data)
            return response
        elif method == "Put":
            response = self.run.put_main(url, data)
            return response
        else:
            print("接口访问出错")

        """
        try:
            # 区分请求方法种类
            if method == "Get":
                response = self.run.get_main(url, data)
            elif method == "Post":
                response = self.run.post_main(url, data)
            elif method == "Delete":
                response = self.run.delete_main(url, data)
            else:
                # method == "Put"
                response = self.run.put_main(url, data)
            return response
        except Exception as e:
            print("接口访问出错")
        """

    # 获取预期结果，方便断言时直接使用
    def get_expect(self, api_name):
        try:
            # 获取配置文件中的预期结果
            expect = self.read.get_expect(api_name)
            print("预期结果为：", expect['success'])
            return expect
        except Exception as e:
            print("获取预期结果出错")
if __name__ == '__main__':
    all_api = AllApi()
    # print("================================== production登录 ==================================")
    # all_api.send_request("query_academyAll")
    print("=================================== 查询所有学院 ====================================")
    all_api.send_request('delete_academy_single(success)')