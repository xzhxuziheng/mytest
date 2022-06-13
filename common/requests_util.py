import requests


class RequestsUtil:

    session = requests.session()

    def send_request(self, method, url, header, data, **kwargs):
        method = str(method).lower()
        res = ''
        if method == 'get':
            res = RequestsUtil.session.request(method=method, url=url, headers=header, params=data, **kwargs)
        elif method == 'post':
            res = RequestsUtil.session.request(method, url, header, json=data, **kwargs)
        elif method == 'put':
            res = RequestsUtil.session.request(method=method, url=url, headers=header, json=data, **kwargs)
        return res


if __name__ == '__main__':
    method = 'post'
    url = 'https://test.rent.ledear.cn/rent-api/account/platform/account/account-info'
    data = {"phone": "19180930619", "code": "930619"}
    header = {'source_type': '3', 'content-type': 'application/json'}
    res = RequestsUtil().send_request(method, url, header, data)
    print(res.json())
    print(res.request.body)
    print(res.headers)
