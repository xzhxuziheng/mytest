import pytest
from common import yaml_util
from common import requests_util
from common.common_util import CommonUtil


class TestOrder:

    domain = CommonUtil.domain
    header = CommonUtil.header

    # 获取骑行订单列表
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/yaml_data/order/rideOrderList.yaml'))
    def test_ride_order(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.domain+caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = caseinfo['data']
        print('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        print(res.json())


if __name__ == '__main__':
    TestOrder()

