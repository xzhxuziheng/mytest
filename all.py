import pytest
import time
import os
from common import allure_util


if __name__ == '__main__':
    pytest.main()
    time.sleep(3)
    os.system('allure generate ./temps -o ./report --clean')
    allure_util.set_windos_title("自动化测试报告")
    report_title = allure_util.get_json_data("自动化测试报告")
    allure_util.write_json_data(report_title)
