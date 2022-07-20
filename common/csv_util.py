import csv
import json
import os
from contextlib import ExitStack

"""
将csv文件转换成json
"""
profileList = []


def get_file_path():
    return os.path.dirname(__file__).split('common')[0]


def fromCsvToJson(csv_path):
    with open(get_file_path()+csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            profileList.append(dict(row))
        return profileList

if __name__ == '__main__':
    print(fromCsvToJson('/all_testcase/case/csv_data/orderPlatformRideList.csv'))
    a = '/all_testcase/case/orderPlatformRideList.yaml'
