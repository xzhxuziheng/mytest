import pytest
from common import yaml_util
from common import requests_util
from conftest import get_token


class TestApi:

    # @pytest.mark.dependency(name='test_api')
    # @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/login.yaml'))
    # def test_api(self, caseinfo):
    #     name = caseinfo['name']
    #     url = caseinfo['url']
    #     method = caseinfo['method']
    #     header = caseinfo['header']
    #     data = caseinfo['data']
    #     res = requests_util.RequestsUtil.session.request(url=url, params=data, method=method, headers=header)
    #     print(res.json())

    # @pytest.mark.dependency(depends=['test_api'])
    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/orderPlatformRideList.yaml'))
    def test_get_depend(self, caseinfo):
        name = caseinfo['name']
        url = caseinfo['url']
        method = caseinfo['method']
        header = caseinfo['header']
        token = {'token': get_token}
        header.update(token)
        data = caseinfo['data']
        print('测试接口：%s' % name)
        res = requests_util.RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        print(res.json())


if __name__ == '__main__':
    TestApi()

