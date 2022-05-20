import pytest
from common import yaml_util
from common.requests_util import RequestsUtil
from common.common_util import CommonUtil


class TestOrderPlatformRide:

    base_url = CommonUtil.base_url
    header = CommonUtil.header
    response_data = []

    # 获取骑行订单列表
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/orderPlatformRideList.yaml'))
    def test_get_order_platform_ride_list(self, caseinfo):
        name = caseinfo['name']
        url = TestOrderPlatformRide.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestOrderPlatformRide.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        print(token)
        header.update(token)
        print(header)
        data = caseinfo['data']
        print('测试接口：%s' % name)
        res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        TestOrderPlatformRide.response_data.append(res.json())

    def get_response_data(self, response_data):
        length = len(response_data)
        if length == 0:
            return ''
        else:
            return response_data

    def get_yaml_depend_data(self, depend_data):
        yaml_file_path = '/xxx.yaml'
        depends = yaml_util.read_yaml(yaml_file_path)['depends']


