import json
from API.all_api import AllApi
import pytest


@pytest.mark.asset
class TestAssetAdd(object):  # 增加 测试用例（正向）
    @pytest.fixture(scope="class")
    def init_asset(self):
        all_request = AllApi()
        return all_request

    @pytest.mark.add  # 新增
    @pytest.mark.parametrize("api_name", ["add_academy_1(success)"])  # 土力院T01
    def test_add_academy_0(self, api_name, init_asset):
        print("\n======用例名称： 新增学院======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text
        """
            还需要增加 添加学院失败：必要参数未填，新增学院失败：添加学院已存在，新增学院失败：json格式错误 三种情况
        """

    @pytest.mark.add  # 新增
    @pytest.mark.parametrize("api_name", ["add_academy_2(success)"])  # 信息院T001
    def test_add_academy_1(self, api_name, init_asset):
        print("\n======用例名称： 新增学院======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text

    @pytest.mark.add  # 新增
    @pytest.mark.parametrize("api_name", ["add_academy_3(success)"])  # 工管院T002
    def test_add_academy_2(self, api_name, init_asset):
        print("\n======用例名称： 新增学院======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text
if __name__ == '__main__':
    pytest.main(['-s', 'test_AddAcademyCase.py', '-m=add'])