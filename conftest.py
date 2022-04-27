import pytest
from common import yaml_util


# @pytest.fixture(scope='function', params=read_yaml(), name='db', autouse=False)
# def exe_database_sql(request):
#     print('执行SQL查询')
#     yield request.param
#     print('关闭数据库连接')


@pytest.fixture(scope='session', autouse=True)
def clean_extract():
    yaml_util.clean_yaml('/web_testcase/case/dependCase.yaml')
