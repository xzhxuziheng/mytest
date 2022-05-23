from common import yaml_util
from common.requests_util import RequestsUtil
from common.common_util import CommonUtil



# base_url = CommonUtil.base_url
# header = CommonUtil.header
# response_data = []
#
#
# def test_get_order_platform_ride_list():
#     caseinfo = yaml_util.read_yaml('/web_testcase/case/mytest.yaml')
#     name = caseinfo['name']
#     url = base_url+caseinfo['url']
#     method = caseinfo['method']
#     token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
#     header.update(token)
#     data = caseinfo['data']
#     res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
#     response_data.append(res.json())
#     return response_data
#
# def test_get_order_platform_ride_list1():
#     caseinfo = yaml_util.read_yaml('/web_testcase/case/mytest.yaml')
#     name = caseinfo['name']
#     url = base_url+caseinfo['url']
#     method = caseinfo['method']
#     token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
#     header.update(token)
#     data = caseinfo['data']
#     res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
#     response_data.append(res.json())
#     return response_data

# def get_response_data(response_data):
#     length = len(response_data)
#     if length == 0:
#         return '依赖字段为空'
#     else:
#         return response_data

def get_yaml_depend_data(yaml_file_path):
    depends = yaml_util.read_yaml(yaml_file_path)[1]['depends']
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
    for depends_key in depends:
        depends_key = depends_key.split('.')
        for i in range(len(depends_key)):
            try:
                msg_data = msg[depends_key[i]]
            except TypeError:
                depends_key[i] = int(depends_key[i])
                msg_data = msg[depends_key[i]]
        return msg_data


        # for dpk in depends_key1:
        #     try:
        #         msg = msg[dpk]
        #         print('我是取值后的msg：%s' % msg)
        #     except TypeError:
        #         dpk = int(dpk)
        #         msg = msg[dpk]
        # print(msg)
# print(test_get_order_platform_ride_list())
# test_get_order_platform_ride_list1()
# print(response_data)
# print(get_yaml_depend_data('/web_testcase/case/mytest.yaml'))
print(get_yaml_depend_data('/web_testcase/case/all_api.yaml'))
# print(yaml_util.read_yaml('/web_testcase/case/all_api.yaml'))
