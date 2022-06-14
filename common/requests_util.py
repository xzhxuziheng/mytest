import requests


class RequestsUtil:

    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        res = ''
        if method == 'get':
            res = RequestsUtil.session.request(method, url, params=data, **kwargs)
        elif method == 'post':
            res = RequestsUtil.session.request(method, url, json=data, **kwargs)
        elif method == 'put':
            res = RequestsUtil.session.request(method, url, json=data, **kwargs)
        return res


if __name__ == '__main__':
    method = 'put'
    url = 'https://test.rent.ledear.cn/rent-api/merchant/platform/merchant/update-status'
    _data = {'status': 1}
    _id = {'id': 159}
    header = {
        'source_type': '3',
        'content-type': 'application/json',
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfdHlwZSI6Mywic291cmNlX2lkIjoxOX0.rFmQIdL4TbEfK-m6_3Kr9k8n1CipEsVFzrgkvzM7A0M'
    }
    res = RequestsUtil().send_request(method, url, _data,  headers=header, params=_id)
    # res = requests.put(url=url, json=_data, headers=header, params=_id)
    print(res.json())
    print(res.request.body)
    print(res.request.headers)
    print(res.request.url)
