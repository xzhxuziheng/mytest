import pytest
from common import yaml_util
from common.requests_util import RequestsUtil
from common.common_util import CommonUtil
from common import log_util


log = log_util.Log(__name__)
logger = log.Logger


class TestAllApi:

    base_url = CommonUtil.base_url
    header = CommonUtil.header
    response_data = []

    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/all_api.yaml'))
    def test_all_api(self, caseinfo):
        logger.info(caseinfo)
        depends = str(caseinfo['depends']).upper()
        logger.info(depends)
        name = caseinfo['name']
        url = TestAllApi.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestAllApi.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = caseinfo['data']
        logger.info('测试接口：%s' % name)
        # 此处for循环有问题
        for i in range(len(caseinfo)):
            if depends == 'N':
                res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
                TestAllApi.response_data.append(res.json())
                logger.info(res.request.headers)
                logger.info(res.request.url)
                logger.info(res.json())
            elif depends == 'Y':
                # 获取全局接口yaml地址
                base_yaml_path = yaml_util.read_yaml('/baseconfig.yaml')['all_api_yaml']
                logger.info(base_yaml_path)
                # 获取依赖key值
                logger.info('我是第%s次取值' % i)
                depends_yaml_path_key = yaml_util.read_yaml(base_yaml_path)[i]['depends_key']
                logger.info(depends_yaml_path_key)
                # 获取依赖value值
                depends_yaml_path_value = yaml_util.read_yaml(base_yaml_path)[i]['depends_value']
                logger.info(depends_yaml_path_value)
                # 保存接口返回字段
                # for depends_value in depends_yaml_path_value:
                get_depends_value = []
                for depends_value in depends_yaml_path_value:
                    depends_value = depends_value.split('.')
                    msg = TestAllApi.response_data
                    logger.info(msg)
                    for depends in depends_value:
                        try:
                            depends = int(depends)
                            logger.info(depends)
                            msg = msg[depends]
                        except:
                            msg = msg[depends]
                            logger.info(depends)
                    get_depends_value.append(msg)
                depends_data = dict(zip(depends_yaml_path_key, get_depends_value))
                data.update(depends_data)
                res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data)
                TestAllApi.response_data.append(res.json())
                logger.info(res.request.headers)
                logger.info(res.request.url)
                logger.info(res.json())
