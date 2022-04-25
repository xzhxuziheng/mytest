import pytest
from common import yaml_util, requests_util


# @pytest.fixture(scope='function', params=read_yaml(), name='db', autouse=False)
# def exe_database_sql(request):
#     print('执行SQL查询')
#     yield request.param
#     print('关闭数据库连接')


@pytest.fixture(scope='session', autouse=True)
def clean_extract():
    yaml_util.clean_yaml('/web_testcase/case/dependCase.yaml')

# @pytest.fixture()
def get_token():
    caseinfo = yaml_util.read_yaml('/web_testcase/case/login.yaml')[0]
    name = caseinfo['name']
    url = caseinfo['url']
    method = caseinfo['method']
    header = caseinfo['header']
    data = caseinfo['data']
    res = requests_util.RequestsUtil.session.request(method=method, url=url, params=data, headers=header)
    print(res.json()['data'])


if __name__ == '__main__':
    print(get_token)