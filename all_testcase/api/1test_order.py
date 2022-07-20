import pytest
from common import log_util
from common import yaml_util
from common import requests_util
from common.common_util import CommonUtil
from common.assert_util import assert_in


log = log_util.Log(__name__)
logger = log.Logger

class TestOrder:

    base_url = CommonUtil.base_url
    header = CommonUtil.header
    # token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token']}

    # 获取骑行订单列表
    @pytest.mark.parametrize('caseinfo', yaml_util.read_new_yaml('/all_testcase/case/yaml_data/base_yaml/orderPlatformRideList.yaml', '/all_testcase/case/yaml_data/order/rideOrderList.yaml', '/all_testcase/case/csv_data/orderPlatformRideList.csv'))
    def test_ride_order_list(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = caseinfo['data']
        asserts = caseinfo['asserts']
        logger.info('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        logger.info(res.json())
        assert_in(asserts, res.json()['message'])
        # 保存骑行订单数据，订单id，订单编号，车辆编号，手机号，订单状态，开始时间，结束时间
        try:
            data = {'rideOrder': {
                'orderRideId': res.json()['data']['list'][0]['id'],
                'orderNo': res.json()['data']['list'][0]['orderNo'],
                'bikeNo': res.json()['data']['list'][0]['bikeNo'],
                'userPhone': res.json()['data']['list'][0]['userPhone'],
                'state': res.json()['data']['list'][0]['state'],
                'startTime': res.json()['data']['list'][0]['startTime'],
                'endTime': res.json()['data']['list'][0]['endTime']}
            }
            yaml_util.write_yaml('/all_testcase/case/dependCase.yaml', data)
        except IOError:
            logger.info('写入骑行订单数据失败')

    # 查询
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/all_testcase/case/yaml_data/order/rideOrderListQuery.yaml'))
    def test_ride_order_list_query(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.base_url + caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token']}
        data = caseinfo['data']
        try:
            depend_data = {
                'orderNo': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['orderNo'],
                'bikeNo': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['bikeNo'],
                'userPhone': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['userPhone'],
                'state': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['state'],
                'startBorrowTime': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['startTime'],
                'endBorrowTime': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['startTime'],
                'startReturnTime': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['endTime'],
                'endReturnTime': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['endTime']
            }
        except KeyError:
            logger.info('获取数据失败')
        header.update(token)
        data.update(depend_data)
        asserts = caseinfo['asserts']
        logger.info('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        assert_in(asserts, res.json()['message'])
        logger.info(res.json())

    # 获取订单详情1
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/all_testcase/case/yaml_data/order/rideOrderInfo.yaml'))
    def test_ride_order_info(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        try:
            data = {'orderRideId': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['orderRideId']}
        except KeyError:
            logger.info('获取数据失败')
        asserts = caseinfo['asserts']
        logger.info('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        assert_in(asserts, res.json()['message'])
        logger.info(res.json())

    # 获取订单详情2
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/all_testcase/case/yaml_data/order/rideOrderDetail.yaml'))
    def test_ride_order_detail(self, caseinfo):
        name = caseinfo['name']
        url = TestOrder.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestOrder.header
        token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        try:
            data = {'orderRideId': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['rideOrder']['orderRideId']}
        except KeyError:
            logger.info('获取数据失败')
        asserts = caseinfo['asserts']
        logger.info('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        assert_in(asserts, res.json()['message'])
        logger.info(res.json())




if __name__ == '__main__':
    TestOrder()

