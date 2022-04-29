from common import yaml_util


class CommonUtil:

    data = yaml_util.read_yaml('/requestOfGlobal.yaml')
    base_url = data['base_url']
    header = data['header']
    login_header = data['login_header']

    # def setup_class(self):
    #     print('每个类之前执行一次')
    #
    #
    # def teardown_class(self):
    #     print('每个类之后执行一次')
    #
    #
    # def setup(self):
    #     print('每个用例之前执行一次')
    #
    #
    # def teardown(self):
    #     print('每个用例之后执行一次')