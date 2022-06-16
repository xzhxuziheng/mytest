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

    @pytest.mark.parametrize('caseinfo', yaml_util.read_yaml('/web_testcase/case/all_api.yaml'))
    def test_all_api(self, caseinfo):
        # logger.info('请求参数：%s' % caseinfo)
        # logger.info('请求参数类型：%s' % type(caseinfo))
        depends = str(caseinfo['depends']).upper()
        # logger.info('是否有接口依赖：%s' % depends)
        num = caseinfo['num']
        name = caseinfo['name']
        url = TestAllApi.base_url+caseinfo['url']
        method = caseinfo['method']
        header = TestAllApi.header
        token = {'token': yaml_util.read_yaml('/web_testcase/case/dependCase.yaml')['token']}
        header.update(token)
        data = caseinfo['data']
        logger.info('测试接口：'+num+'%s' % name)
        if depends == 'N':
            res = RequestsUtil().send_request(method, url, data, headers=header)
            yaml_util.write_yaml('/web_testcase/case/response.yaml', {num: res.json()})
            # logger.info('请求头：%s' % res.request.headers)
            # logger.info('请求路径：%s' % res.request.url)
            # logger.info('响应结果：%s' % res.json())
        elif depends == 'Y':
            depends_site = caseinfo['depends_site']
            depends_type = caseinfo['depends_type']
            # 获取依赖key值
            depends_yaml_path_key = caseinfo['depends_key']
            # logger.info('写入依赖的key值：%s' % depends_yaml_path_key)
            # 获取依赖value值
            depends_yaml_path_value = caseinfo['depends_value']
            # logger.info('写入依赖的value路径：%s' % depends_yaml_path_value)
            get_depends_value = []
            for depends_value in depends_yaml_path_value:
                depends_value = depends_value.split('.')
                msg = yaml_util.read_yaml('/web_testcase/case/response.yaml')
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
            if depends_type == 'str':
                depends_data = dict(zip(depends_yaml_path_key, get_depends_value))
            elif depends_type == 'list':
                depends_data = dict(zip(depends_yaml_path_key, [get_depends_value]))
            logger.info('我是depends_data：%s' % depends_data)
            logger.info('我是depends_data类型：%s' % type(depends_data))
            if depends_site == 'body' or depends_site is None:
                if data is None:
                    data = {}
                    data.update(depends_data)
                else:
                    data.update(depends_data)
                res = RequestsUtil().send_request(method, url, data, headers=header)
                yaml_util.write_yaml('/web_testcase/case/response.yaml', {num: res.json()})
            elif depends_site == 'url':
                res = RequestsUtil().send_request(method, url, data, headers=header, params=depends_data)
                yaml_util.write_yaml('/web_testcase/case/response.yaml', {num: res.json()})
        res.content.decode("unicode-escape")
        logger.info('请求头：%s' % res.request.headers)
        logger.info('请求路径：%s' % res.request.url)
        try:
            # 输出\u编码将其转换成中文 eg：\\u56db\\u5ddd\\u7701\\u6210\\u90fd\\u5e02\\u6b66\\u4faf\\u533a\\u77f3
            logger.info('请求参数：%s' % res.request.body.decode("unicode-escape"))
        except AttributeError:
            logger.info('请求参数：%s' % res.request.body)
        logger.info('响应结果：%s' % res.json())
