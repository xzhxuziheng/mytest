import pytest
from common import yaml_util
from common import db_util

# @pytest.fixture(scope='function', params=read_yaml(), name='db', autouse=False)
# def exe_database_sql(request):
#     print('执行SQL查询')
#     yield request.param
#     print('关闭数据库连接')


@pytest.fixture(scope='session', autouse=True)
def clean_extract():
    yaml_util.clean_yaml('/web_testcase/case/dependCase.yaml')
    yaml_util.clean_yaml('web_testcase/case/response.yaml')


@pytest.fixture(scope='session', autouse=True)
def db_delete():
    sql_data_delete = yaml_util.read_yaml('/web_testcase/case/mysql.yaml')['delete']
    db_util.handle_mysql(sql_data_delete)
