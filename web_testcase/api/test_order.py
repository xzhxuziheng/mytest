import pytest
from common import yaml_util
from common import requests_util
from common.common_util import CommonUtil


class TestOrder:

    base_url = CommonUtil.base_url
    header = CommonUtil.header
    # token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}

    # 获取骑行订单列表
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/yaml_data/order/rideOrderList.yaml'))
    def test_ride_order_list(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = caseinfo['data']
        print('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        print(res.json())
        # 保存骑行订单数据，订单id，订单编号，车辆编号，手机号，订单状态，开始时间，结束时间
        try:
            data = {
                'orderRideId': res.json()['data']['list'][0]['id'],
                'orderNo': res.json()['data']['list'][0]['orderNo'],
                'bikeNo': res.json()['data']['list'][0]['bikeNo'],
                'userPhone': res.json()['data']['list'][0]['userPhone'],
                'state': res.json()['data']['list'][0]['state'],
                'startTime': res.json()['data']['list'][0]['startTime'],
                'endTime': res.json()['data']['list'][0]['endTime']
            }
            yaml_util.write_yaml('/web_testcase/case/dependCase.yaml', data)
        except:
            print('获取骑行订单数据失败')

    # 查询
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/yaml_data/order/rideOrderListQuery.yaml'))
    def test_ride_order_list_query(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.base_url + caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        data = caseinfo['data']
        depend_data = {
            'orderNo': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['orderNo'],
            'bikeNo': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['bikeNo'],
            'userPhone': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['userPhone'],
            'state': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['state'],
            'startBorrowTime': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['startTime'],
            'endBorrowTime': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['startTime'],
            'startReturnTime': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['endTime'],
            'endReturnTime': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['endTime']
        }
        header.update(token)
        data.update(depend_data)
        print('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        print(res.json())

    # 获取订单详情
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/yaml_data/order/rideOrderInfo.yaml'))
    def test_ride_order_info(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = {'orderRideId': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['orderRideId']}
        print('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        print(res.json())

    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/yaml_data/order/rideOrderDetail.yaml'))
    def test_ride_order_detail(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = {'orderRideId': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['orderRideId']}
        print('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        print(res.json())




if __name__ == '__main__':
    TestOrder()

