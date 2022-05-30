import os
import time
import yaml


class ReadYaml(object):
    def read_yml(self):
        # 获取配置文件路径
        curPath = os.path.abspath(os.path.dirname(__file__))
        yamlPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "metadata/api.yaml")
        # print(yamlPath)

        f = open(yamlPath, 'r', encoding='utf-8')

        content = f.read()
        contents = yaml.load(content, Loader=yaml.FullLoader)
        # print(type(content))
        # print("文件中所有内容：", contents)
        # print("登录接口内容：", contents['host'])

        return contents

    def get_url(self, api_name):
        content = self.read_yml()
        new_url = content['host']+content[api_name]['url']
        print("请求地址： ", new_url)
        return new_url

    def get_method(self, api_name):
        content = self.read_yml()
        print("请求方式： ", content[api_name]['method'])
        return content[api_name]['method']

    def get_data(self, api_name):
        content = self.read_yml()
        print("请求数据： ", content[api_name]['data'])
        return content[api_name]['data']

    def get_expect(self, api_name):
        content = self.read_yml()
        expected = content[api_name]['expected']
        return expected

    def get_time(self):
        # 以毫秒为单位的时间戳
        get_now_milli_time = int(time.time() * 1000)
        print(get_now_milli_time)

if __name__ == '__main__':
    y = ReadYaml()
    print("delete_academy_single(success)")
    y.get_url('delete_academy_single(success)')
    y.get_method("delete_academy_single(success)")
    y.get_data("delete_academy_single(success)")
    print(type(y.get_data("delete_academy_single(success)")))