import pytest
from common import yaml_util
from common.assert_util import assert_in
from common.requests_util import RequestsUtil
from common.common_util import CommonUtil
from common import log_util


log = log_util.Log(__name__)
logger = log.Logger


class TestAllApi:

    base_url = CommonUtil.base_url
    # header_admin = CommonUtil.header_admin
    # header_factory_wx_mini = CommonUtil.header_factory_wx_mini

    # 获取依赖
    def get_depends(self, data):
        get_depends_value = []
        for depends_value in data:
            depends_value = depends_value.split('.')
            msg = yaml_util.read_yaml('/all_testcase/case/response.yaml')
            # logger.info('读取保存在yaml的数据：%s' % msg)
            for value in depends_value:
                try:
                    value = int(value)
                    # logger.info('拆分依赖路径：%s' % value)
                    msg = msg[value]
                except:
                    msg = msg[value]
                    # logger.info('拆分依赖路径：%s' % value)
            get_depends_value.append(msg)
        return get_depends_value

    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/all_testcase/case/all_api.yaml'))
    def test_all_api(self, caseinfo):
        execute = str(caseinfo['execute'])[-1].upper()
        # 用例是否执行
        if execute == 'Y':
            # logger.info('请求参数：%s' % caseinfo)
            # logger.info('请求参数类型：%s' % type(caseinfo))
            depends = str(caseinfo['depends']).upper()
            # logger.info('是否有接口依赖：%s' % depends)
            num = caseinfo['num']
            name = caseinfo['name']
            url = TestAllApi.base_url+caseinfo['url']
            method = caseinfo['method']
            token_source = caseinfo['token_source']
            header = ''
            token = ''
            # web平台端token
            if token_source == 'admin':
                header = CommonUtil.header_admin
                token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token_admin']}
            # web运营商端token
            elif token_source == 'operator':
                token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token_operator']}
            # 商户端app token
            elif token_source == 'merchant_app':
                token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token_merchant_app']}
            # 厂测微信小程序token
            elif token_source == 'factory_wx_mini':
                header = CommonUtil.header_factory_wx_mini
                token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token_factory_wx_mini']}
            # 用户端微信小程序token
            elif token_source == 'user_wx_mini':
                header = CommonUtil.header_user_wx_mini
                token = {'token': yaml_util.read_yaml('/all_testcase/case/dependCase.yaml')['token_user_wx_mini']}
            header.update(token)
            data = caseinfo['data']
            if data is None:
                data = {}
            asserts = caseinfo['asserts']
            logger.info('测试接口：'+num+'%s' % name)
            res = ''
            if depends == 'N':
                res = RequestsUtil().send_request(method, url, data, headers=header)
                yaml_util.write_yaml('/all_testcase/case/response.yaml', {num: res.json()})
                # 断言失败结果写入日志
                assert_in(asserts, res.json()['message'])
                assert asserts in res.json()['message']
            elif depends == 'Y':
                depends_site = caseinfo['depends_site']
                depends_type = caseinfo['depends_type']
                if depends_site == 'body' or depends_site is None:
                    # 获取依赖key值
                    depends_key = caseinfo['depends_key']
                    # 获取依赖value值
                    depends_value = caseinfo['depends_value']
                    get_depends_value = TestAllApi().get_depends(depends_value)
                    # 依赖拼接成{"id": 1}
                    depends_data = ''
                    if depends_type == 'str':
                        depends_data = dict(zip(depends_key, get_depends_value))
                    # 依赖拼接成{"id": [1]}
                    elif depends_type == 'list':
                        depends_data = dict(zip(depends_key, [get_depends_value]))
                    logger.info('我是depends_data：%s' % depends_data)
                    logger.info('我是depends_data类型：%s' % type(depends_data))
                    if data is None:
                        data = {}
                        data.update(depends_data)
                    else:
                        data.update(depends_data)
                    res = RequestsUtil().send_request(method, url, data, headers=header)
                    yaml_util.write_yaml('/all_testcase/case/response.yaml', {num: res.json()})
                    assert_in(asserts, res.json()['message'])
                    assert asserts in res.json()['message']
                elif depends_site == 'url':
                    depends_key = caseinfo['depends_key']
                    depends_value = caseinfo['depends_value']
                    get_depends_value = TestAllApi().get_depends(depends_value)
                    depends_data = ''
                    if depends_type == 'str':
                        depends_data = dict(zip(depends_key, get_depends_value))
                    elif depends_type == 'list':
                        depends_data = dict(zip(depends_key, [get_depends_value]))
                    logger.info('我是depends_data：%s' % depends_data)
                    logger.info('我是depends_data类型：%s' % type(depends_data))
                    res = RequestsUtil().send_request(method, url, data, headers=header, params=depends_data)
                    yaml_util.write_yaml('/all_testcase/case/response.yaml', {num: res.json()})
                    assert_in(asserts, res.json()['message'])
                    assert asserts in res.json()['message']
                elif depends_site == 'url_and_body':
                    depends_url_key = caseinfo['depends_url_key']
                    depends_url_value = caseinfo['depends_url_value']
                    depends_body_key = caseinfo['depends_body_key']
                    depends_body_value = caseinfo['depends_body_value']
                    get_depends_url_value = TestAllApi().get_depends(depends_url_value)
                    get_depends_body_value = TestAllApi().get_depends(depends_body_value)
                    depends_url_data = dict(zip(depends_url_key, get_depends_url_value))
                    depends_body_data = dict(zip(depends_body_key, get_depends_body_value))
                    data.update(depends_body_data)
                    res = RequestsUtil().send_request(method, url, data, headers=header, params=depends_url_data)
                    yaml_util.write_yaml('/all_testcase/case/response.yaml', {num: res.json()})
                    assert_in(asserts, res.json()['message'])
                    assert asserts in res.json()['message']
            # 返回二进制数据
            # res.content.decode("unicode-escape")
            logger.info('请求头：%s' % res.request.headers)
            logger.info('请求路径：%s' % res.request.url)
            try:
                # 输出\u编码将其转换成中文 eg：\\u56db\\u5ddd\\u7701\\u6210\\u90fd\\u5e02\\u6b66\\u4faf\\u533a\\u77f3
                logger.info('请求参数：%s' % res.request.body.decode("unicode-escape"))
            except AttributeError:
                logger.info('请求参数：%s' % res.request.body)
            logger.info('响应结果：%s' % res.json())
        else:
            logger.info('接口不执行：%s%s' % (caseinfo['num'], caseinfo['name']))
