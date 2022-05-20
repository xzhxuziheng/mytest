import json


data = {'code': '00000', 'message': '成功', 'data': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfdHlwZSI6Mywic291cmNlX2lkIjo0MX0.jgBWGSF8KBYko8gttLam-SqcH9xHzgSkT2sgaRaIzzo'}
assert '成功' == data['message']
