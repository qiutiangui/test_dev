import os
from string import Template

import requests
import yaml
from jmespath import search
import random

def login():
    # datapath = os.path.join(os.path.abspath('..'), "data")
    # filepath = os.path.join(datapath, "login.yml")
    #
    # aa = ReadYaml(filepath)
    # data = aa.read_yaml()
    #
    # url = search('test01.request.url', data)
    # body = search('test01.request.body', data)
    # headers = search('test01.request.headers', data)

    url = "https://api.xdclass.net/pub/api/v1/web/web_login"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    body = {"phone": "15626592199", "pwd": "755899tian"}

    response = requests.post(url, data=body, headers=headers).json()
    print(response)
    token = search('data.token', response)
    return token


def number():
    return random.randint(10000000000000, 9999999999999)


if __name__ == '__main__':
    login()
