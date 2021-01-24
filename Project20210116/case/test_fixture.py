import pytest


def test_login01():
    print("测试用例1")


def test_login02():
    print("测试用例2")


def test_login03():
    print("测试用例3")


if __name__ == '__main__':
    pytest.main(["-s","test_fixture.py"])
