import pytest
from common import yaml_util
from common import db_util


@pytest.fixture(scope='session', autouse=True)
def clean_extract():
    yaml_util.clean_yaml('all_testcase/case/dependCase.yaml')
    yaml_util.clean_yaml('all_testcase/case/response.yaml')


@pytest.fixture(scope='session', autouse=True)
def db_delete():
    sql_data_delete = yaml_util.read_yaml('all_testcase/case/mysql.yaml')['delete']
    db_util.handle_mysql(sql_data_delete)

@pytest.fixture(scope='session', autouse=True)
def db_insert():
    sql_data_insert = yaml_util.read_yaml('all_testcase/case/mysql.yaml')['insert']
    db_util.handle_mysql(sql_data_insert)
