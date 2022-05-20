import requests


class RequestsUtil:

    session = requests.session()

    def send_request(self,method, url, data, **kwargs):
        method = str(method).lower()
        res = ''
        if method == 'get':
            res = RequestsUtil.session.request(method, url, params=data, **kwargs)
        elif method == 'post':
            res = RequestsUtil.session.request(method, url, json=data, **kwargs)
        return res
