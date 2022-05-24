from common import yaml_util
from common.requests_util import RequestsUtil
from common.common_util import CommonUtil


def get_yaml_depends_data(yaml_file_path, data):
    depends_data = yaml_util.read_yaml(yaml_file_path)[1][data]
    return depends_data


def get_yaml_depends_value():
    depends_value = get_yaml_depends_data('/web_testcase/case/all_api.yaml', 'depends_value')
    get_depends_value = []
    for dv in depends_value:
        dv = dv.split('.')
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
        for depends in dv:
            try:
                depends = int(depends)
                msg = msg[depends]
            except:
                msg = msg[depends]
        get_depends_value.append(msg)
    return get_depends_value

def get_depends_key_value():
    depends_key = get_yaml_depends_data('/web_testcase/case/all_api.yaml', 'depends_key')
    depends_value = get_yaml_depends_value()
    return dict(zip(depends_key, depends_value))

# print(test_get_order_platform_ride_list())
# test_get_order_platform_ride_list1()
# print(response_data)
# print(get_yaml_depend_data('/web_testcase/case/mytest.yaml'))
print(get_depends_key_value())
# print(yaml_util.read_yaml('/web_testcase/case/all_api.yaml'))
