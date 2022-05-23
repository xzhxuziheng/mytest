import pytest
from common import yaml_util
from common.requests_util import RequestsUtil
from common.common_util import CommonUtil


class TestAllApi:

    base_url = CommonUtil.base_url
    header = CommonUtil.header
    response_data = []

    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/all_api.yaml'))
    def test_get_order_platform_ride_list(self, caseinfo):
        name = caseinfo['name']
        url = TestAllApi.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestAllApi.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = caseinfo['data']
        res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        TestAllApi.response_data.append(res.json())

    def get_response_data(self, response_data):
        length = len(response_data)
        if length == 0:
            return ''
        else:
            return response_data

    def get_yaml_depend_data(self):
        yaml_file_path = '/web_testcase/case/mytest.yaml'
        depends = yaml_util.read_yaml(yaml_file_path)['depends']
        print(TestOrderPlatformRide.response_data[depends])

t = TestOrderPlatformRide()
print(t.get_yaml_depend_data())


