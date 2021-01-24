import pytest

"""
pytest.mark.skip 可以标记无法在某些平台上运行的测试功能，戒
者您希望失败的测试功能
"""
# @pytest.mark.skip 标记之后会跳过该用例，该用例不会执行
@pytest.mark.skip
def test_01():
    print("测试用例1")


def test_02():
    print("测试用例2")


def test_03():
    print("测试用例3")


if __name__ == '__main__':
    pytest.main(["-s", "test_skip.py"])
