import pytest

"""
pytest 可以支持自定义标记，自定义标记可以把一个 web 顷目划
分多个模块，然后指定模块名称执行。app 自动化的时候，如果想
 第 72 / 346 页 个人博客：https://www.cnblogs.com/yoyoketang/
 《python 自动化框架 pytest》 作者：上海-悠悠 QQ 群：874033608
android 呾 ios 公用一套代码时，
也可以使用标记功能，标明哪些是 ios 用例，哪些是 android 的，运行
代码时候指定 mark 名称运行就可以
"""


@pytest.mark.ios
def test_login01():
    print("测试用例1")


def test_login02():
    print("测试用例2")


def test_login03():
    print("测试用例3")


if __name__ == '__main__':
    pytest.main(["-s", "test_mark.py", "-m=ios"])
