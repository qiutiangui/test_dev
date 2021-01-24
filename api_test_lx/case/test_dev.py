import pytest
import os
import json
from jmespath import search
import requests

from common.read_yml import ReadYaml

datapath = os.path.join(os.path.abspath('..'), "data")


class TestDev:
    """
    登录接口
    """

    def test_query(self):
        """成功"""
        filepath = os.path.join(datapath, "query.yml")
        data1 = ReadYaml(filepath).read_yaml()

        confpath = os.path.join(datapath, "conftest.yml")
        data2 = ReadYaml(confpath).read_yaml()

        url = search('ip.testip1', data2) + search('test01.request.url', data1)
        method = search('test01.request.method', data1)
        headers = search('test01.request.headers', data1)
        body = search('test01.request.body', data1)
        code = search('test01.request.code', data1)

        response = RequestUtil().request(url, method=method, headers=headers, param=body, content_type='data')
        print(response)
        assert search('code', response) == 0


if __name__ == '__main__':
    pytest.main(['-s', 'test_dev.py'])
