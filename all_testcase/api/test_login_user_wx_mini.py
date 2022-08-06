import pytest
from common.common_util import CommonUtil
from common import yaml_util
from common.requests_util import RequestsUtil
from common import log_util
from common.assert_util import assert_in
from common.redis_util import get_redis_data

log = log_util.Log(__name__)
logger = log.Logger

@pytest.mark.run(order=3)
class TestLoginUserWxMini(CommonUtil):

    base_url = CommonUtil.base_url
    login_header = CommonUtil.login_header_factory_wx_mini

    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/all_testcase/case/login_user_wx_mini.yaml'))
    def test_login(self, caseinfo):
        name = caseinfo['name']
        user_key = caseinfo['user_key']
        token_user_wx_mini = get_redis_data(user_key)
        logger.info('测试接口：%s' % name)
        try:
            yaml_data = {'token_user_wx_mini': token_user_wx_mini}
            yaml_util.write_yaml('/all_testcase/case/dependCase.yaml', yaml_data)
        except IOError:
            logger.info('写入token失败')


if __name__ == '__main__':
    pytest.main()
