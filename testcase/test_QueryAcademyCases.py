import json

from API.all_api import AllApi
import pytest

# from common.get_log import get_log

"""
    python装饰器：修改其他函数的功能的函数，在不改变原函数的前提下，增加功能。
"""

"""
    @pytest.mark.自定义标签：用于标记测试用例，方便运行时筛选。同一个测试类/方法可以同时拥有多个标记。
    运行方法：
            pytest -m"自定义标签名"
        或
            pytest.main(['-m自定义标签名'])
"""


@pytest.mark.asset
@pytest.mark.usefixtures
class TestAssetQuery(object):   # 查询 操作测试用例（正向）
    @pytest.fixture(scope="class")
    def init_asset(self):
        all_request = AllApi()
        return all_request

    @pytest.mark.query  # 查询
    @pytest.mark.parametrize("api_name", ["query_academyAll(success)"])  # 参数化
    def test_query_all(self, api_name, init_asset):
        print("\n======用例名称： 查询所有学院======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text  # 此处需要注意比较对象的数据类型
        """
            res.text: str
            excepted：dic
            json.loads: 将json对象转换为python对象 str -> dic
            json.load: 对json进行读取，结果数据类型为list
            json.dumps： 将python对象转换为json对象 dic -> str
            json.dump: 编码，写入json 
            从yaml文件读取的为str，requests请求返回的数据为response
        """
        # assert res.status_code == 200, print("success!!!!!!!!!!!")

    @pytest.mark.query
    @pytest.mark.parametrize("api_name", ["query_academyAppoint(success)"])
    def test_query_appoint(self, api_name, init_asset):
        print("\n======用例名称：查询指定学院======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text

    @pytest.mark.query
    @pytest.mark.parametrize("api_name", ["query_academyAppointID(success)"])
    def test_query_appoint_id(self, api_name, init_asset):
        print("\n======用例名称：根据ID查询指定学院======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text

    @pytest.mark.query
    @pytest.mark.parametrize("api_name", ["query_academyAppointMaster(success)"])
    def test_query_appoint_master_name(self, api_name, init_asset):
        print("\n======用例名称：根据院长名称查询指定学院======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text

    @pytest.mark.query
    @pytest.mark.parametrize("api_name", ["query_academyBlur(success)"])
    def test_query_blur(self, api_name, init_asset):
        print("\n======用例名称：模糊查询======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text

    @pytest.mark.query
    @pytest.mark.parametrize("api_name", ["query_academyCombin(success)"])
    def test_query_blur(self, api_name, init_asset):
        print("\n======用例名称：组合查询======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text


if __name__ == '__main__':
    # 若存在多个标记，则用or连接，形成一个测试集，比如‘-m=assetList or test or allLists’
    # pytest.main(['-s', 'test_QueryAcademyCases.py', '-m=query'])
    pytest.main(['-s', 'test_QueryAcademyCases.py', '-m=query'])