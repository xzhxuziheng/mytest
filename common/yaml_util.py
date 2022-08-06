from contextlib import ExitStack
from common import csv_util
import yaml
import os
import re
import pytest


def get_file_path():
    return os.path.dirname(__file__).split('common')[0]


def read_yaml(yaml_file_path):
    get_file = get_file_path()+yaml_file_path
    with open(file=get_file, mode='r', encoding='utf-8') as f:
        value = yaml.safe_load(f)
        return value


def write_yaml(yaml_file_path, data):
    get_file = get_file_path()+yaml_file_path
    with open(file=get_file, mode='a', encoding='utf-8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def clean_yaml(yaml_file_path):
    get_file = get_file_path() + yaml_file_path
    with open(file=get_file, mode='w', encoding='utf-8') as f:
        f.truncate()


def csvReplaceYaml(yaml_file_path, new_yaml_file_path, csv_path):
    try:
        with ExitStack() as stack:
            yaml_file = stack.enter_context(open(get_file_path()+yaml_file_path, 'r+', encoding='utf-8'))
            yaml_output = stack.enter_context(open(get_file_path()+new_yaml_file_path, 'w', encoding='utf-8'))
            # 先读取YAML模板文件，返回值为字符串列表
            yml_file_lines = yaml_file.readlines()
            profileList = csv_util.fromCsvToJson(csv_path)
            # profileList的长度即为测试用例的数量
            for i in range(0, len(profileList)):
                # 循环遍历列表
                for line in yml_file_lines:
                    new_line = line
                    # 如果找到以“${”开头的字符串
                    if new_line.find('${') > 0:
                        env_list = re.findall(r'\${(.*?)}', new_line)
                        env_value = profileList[i][env_list[0]]
                        new_line = new_line.replace('$'+'{'+env_list[0]+'}', env_value)
                    # 将new_line写入到yml_output文件里
                    yaml_output.write(new_line)
                yaml_output.write("\n\n")
    except IOError as e:
        print("Error: " + format(str(e)))
        raise


def read_new_yaml(yaml_file_path, new_yaml_file_path, csv_path):
    csvReplaceYaml(yaml_file_path, new_yaml_file_path, csv_path)
    return read_yaml(new_yaml_file_path)


if __name__ == '__main__':
    yaml_file_path = '/all_testcase/case/mytest.yaml'
    print(read_yaml(yaml_file_path))
    # print(read_yaml(yaml_file_path)['token_factory_wx_mini'])
    # class Testapi:
    #     @pytest.mark.parametrize('caseinfo', read_yaml(yaml_file_path))
    #     def test_api(self, caseinfo):
    #         print(1111)
