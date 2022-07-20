from common import yaml_util


def get_yaml_depends_data(yaml_file_path, data):
    depends_data = yaml_util.read_yaml(yaml_file_path)[data]
    return depends_data


def get_yaml_depends_value(data):
    depends_value = get_yaml_depends_data('all_testcase/case/all_api.yaml', 'depends_value')
    get_depends_value = []
    for dv in depends_value:
        dv = dv.split('.')
        msg = data
        for depends in dv:
            try:
                depends = int(depends)
                msg = msg[depends]
            except:
                msg = msg[depends]
        get_depends_value.append(msg)
    return get_depends_value


def get_depends_key_value(data):
    depends_key = get_yaml_depends_data('all_testcase/case/all_api.yaml', 'depends_key')
    depends_value = get_yaml_depends_value(data)
    return dict(zip(depends_key, depends_value))