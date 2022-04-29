import pytest
from common.common_util import CommonUtil
from common import yaml_util
from common.requests_util import RequestsUtil


@pytest.mark.run(order=1)
class TestLogin(CommonUtil):

    base_url = CommonUtil.base_url
    login_header = CommonUtil.login_header

    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/login.yaml'))
    def test_login(self, caseinfo):
        name = caseinfo['name']
        url = TestLogin.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestLogin.login_header
        data = caseinfo['data']
        print('测试接口：%s' % name)
        res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
        try:
            yaml_data = {'token': res.json()['data']}
            yaml_util.write_yaml('/web_testcase/case/dependCase.yaml', yaml_data)
        except:
            print('登录失败')


