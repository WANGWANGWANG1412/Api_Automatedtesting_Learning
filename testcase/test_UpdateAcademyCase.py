import json
from API.all_api import AllApi
import pytest


@pytest.mark.asset
class TestAssetAdd(object):  # 更新 测试用例（正向）
    @pytest.fixture(scope="class")
    def init_asset(self):
        all_request = AllApi()
        return all_request

    @pytest.mark.update  # 新增
    @pytest.mark.parametrize("api_name", ["update_academy(success)"])  # 参数化
    def test_update_academy(self, api_name, init_asset):
        print("\n======用例名称： 更新学院信息======")
        res = init_asset.send_request(api_name)
        expected = init_asset.get_expect(api_name)
        assert json.loads(res.text) == expected['success'], "success的值为： %s" % res.text
        """
            还需要增加 添加学院失败：必要参数未填，新增学院失败：添加学院已存在，新增学院失败：json格式错误 三种情况
        """
if __name__ == '__main__':
    pytest.main(['-s', 'test_UpdateAcademyCase.py', '-m=update'])