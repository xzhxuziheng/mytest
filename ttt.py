from common import yaml_util
from common.requests_util import RequestsUtil
from common.common_util import CommonUtil
import time


msg = [{'code': '00000', 'message': '成功', 'data': {'total': 339, 'list': [
            {'id': 10149, 'orderNo': '4122051317291800491525', 'userPhone': '19180930619', 'bikeNo': '1000991',
             'mileage': 0.0, 'payableMoney': 11, 'paidTotalMoney': 0, 'state': 4,
             'startTime': '2022-05-13 17:29:18', 'endTime': '2022-05-13 17:29:23', 'groupId': 7},
            {'id': 10148, 'orderNo': '4122051316402682441525', 'userPhone': '19180930619', 'bikeNo': '1000991',
             'mileage': 0.0, 'payableMoney': 11, 'paidTotalMoney': 0, 'state': 4,
             'startTime': '2022-05-13 16:40:26', 'endTime': '2022-05-13 16:40:30', 'groupId': 7},
            {'id': 10147, 'orderNo': '4122051316362710341525', 'userPhone': '19180930619', 'bikeNo': '1000991',
             'mileage': 0.0, 'payableMoney': 11, 'paidTotalMoney': 0, 'state': 2,
             'startTime': '2022-05-13 16:36:27', 'endTime': '2022-05-13 16:36:32', 'groupId': 7}]}}]

readYaml = yaml_util.read_yaml('/web_testcase/case/all_api.yaml')
depends_key = readYaml[1]['depends_value']
print(depends_key)
for get_key in depends_key:
    list_key = get_key.split('.')
    for str_key in list_key:
        try:
            str_key = int(str_key)
            get_value = yaml_util.read_yaml('/test.yaml')[str_key]
        except:
            get_value = yaml_util.read_yaml('/test.yaml')[str_key]
    print(get_value)
