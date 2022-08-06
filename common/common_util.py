from common import yaml_util


class CommonUtil:

    data = yaml_util.read_yaml('/baseconfig.yaml')
    base_url = data['base_url']
    header_admin = data['header']['admin']
    login_header_admin = data['login_header']['admin']
    header_factory_wx_mini = data['header']['factory_wx_mini']
    login_header_factory_wx_mini = data['login_header']['factory_wx_mini']
    header_user_wx_mini = data['header']['user_wx_mini']
    login_header_user_wx_mini = data['login_header']['user_wx_mini']
