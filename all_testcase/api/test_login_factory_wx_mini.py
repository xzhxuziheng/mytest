import pytest
from common.common_util import CommonUtil
from common import yaml_util
from common.requests_util import RequestsUtil
from common import log_util
from common.assert_util import assert_in


log = log_util.Log(__name__)
logger = log.Logger

@pytest.mark.run(order=2)
class TestLoginFactoryWxMini(CommonUtil):

    base_url = CommonUtil.base_url
    login_header = CommonUtil.login_header_factory_wx_mini

    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/all_testcase/case/login_factory_wx_mini.yaml'))
    def test_login(self, caseinfo):
        name = caseinfo['name']
        url = TestLoginFactoryWxMini.base_url + caseinfo['url']
        method = caseinfo['method']
        header = TestLoginFactoryWxMini.login_header
        data = caseinfo['data']
        asserts = caseinfo['asserts']
        logger.info('测试接口：%s' % name)
        res = ''
        try:
            res = RequestsUtil().send_request(method, url, data, headers=header)
        except SystemError:
            logger.error('登录失败')
        assert_in(asserts, res.json()['message'])
        logger.info(res.request.url)
        logger.info(res.json())
        try:
            yaml_data = {'token_factory_wx_mini': res.json()['data']}
            yaml_util.write_yaml('/all_testcase/case/dependCase.yaml', yaml_data)
        except IOError:
            logger.info('写入token失败')


if __name__ == '__main__':
    pytest.main()
