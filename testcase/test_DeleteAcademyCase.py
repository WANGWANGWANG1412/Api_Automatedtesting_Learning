import json
from API.all_api import AllApi
import pytest


@pytest.mark.asset
class TestAssetAdd(object):  # 删除 测试用例（正向）
    @pytest.fixture(scope="class")
    def init_asset(self):
        all_request = AllApi()
        return all_request

    @pytest.mark.delete  # 删除
    @pytest.mark.parametrize("api_name", ["delete_academy_single(success)"])  # 删除T01
    def test_delete_academy_single(self, api_name, init_asset):
        print("\n======用例名称： 删除学院信息======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        assert res.status_code == int(expected['status_code']), "status_code的值为： %s" % res.status_code

    @pytest.mark.delete  # 删除
    @pytest.mark.parametrize("api_name", ["delete_academy_multiple(success)"])  # 删除T001,T002
    def test_delete_academy_multiple(self, api_name, init_asset):
        print("\n======用例名称： 删除多个学院信息======")
        res = init_asset.send_request(api_name)
        # 获取某接口下的预期返回结果
        expected = init_asset.get_expect(api_name)
        print(type(res.status_code))
        assert res.status_code == int(expected['status_code']), "status_code的值为： %s" % res.status_code

if __name__ == '__main__':
    pytest.main(['-s', 'test_DeleteAcademyCase.py', '-m=delete'])