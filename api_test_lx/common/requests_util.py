import requests


class RequestUtil:
    def __init__(self):
        pass

    def request(self, url, method, headers=None, param=None, content_type=None):
        """通用请求工具类"""
        try:
            if method == 'get':
                result = requests.get(url=url, params=param, headers=headers).json()
                return result
            elif method == 'post':
                if content_type is None:
                    result = requests.post(url=url, json=param, headers=headers).json()
                    return result
                else:
                    result = requests.post(url=url, data=param, headers=headers).json()
                    return result
            else:
                print("http method not allowed")
        except Exception as e:
            print(f'http请求报错：{e}')


if __name__ == '__main__':
    url = "https://api.xdclass.net/pub/api/v1/web/web_login"
    r = RequestUtil()
    data = {"phone": "15626592199", "pwd": "755899tian"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    result = r.request(url, 'post', param=data, headers=headers, content_type='data')
    print(result.json())
