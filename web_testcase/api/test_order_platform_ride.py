import pytest
from common import yaml_util
from common.requests_util import RequestsUtil


class TestOrderPlatformRide:
    # 获取骑行订单列表
    @pytest.mark.parametrize('caseinfo', yaml_util.read_new_yaml('/web_testcase/case/orderPlatformRideList.yaml',
                                                                 '/web_testcase/case/yaml_data/orderPlatformRideList.yaml',
                                                                 '/web_testcase/case/csv_data/orderPlatformRideList.csv'))
    def test_get_order_platform_ride_list(self, caseinfo):
        name = caseinfo['name']
        url = caseinfo['url']
        method = caseinfo['method']
        header = caseinfo['header']
        header.update(yaml_util.read_yaml('/web_testcase/case/dependCase.yaml'))
        data = caseinfo['data']
        print('测试接口：%s' % name)
        res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        try:
            yaml_data = {'orderRideId': res.json()['data']['list'][0]['id']}
            yaml_util.write_yaml('/web_testcase/case/dependCase.yaml', yaml_data)
        except:
            print('获取失败')

    #获取骑行订单详情
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/orderPlatformRideListDetail.yaml'))
    def test_get_order_platform_ride_list_detail(self, caseinfo):
        name = caseinfo['name']
        url = caseinfo['url']
        method = caseinfo['method']
        header = caseinfo['header']
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = {'orderRideId': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['orderRideId']}
        print('测试接口：%s' % name)
        res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        print(res.json())
        print('git test')

