import pytest


# function，每条测试用例均执行一次
@pytest.fixture(scope="function", autouse=True)
def login01():
    print("function")
    yield
    print("测试用例之后执行，如清理数据，释放资源")


# class，每个类执行一次
@pytest.fixture(scope="class", autouse=True)
def login02():
    print("class")


# module，每个模块执行一次
@pytest.fixture(scope="module", autouse=True)
def login03():
    print("module")

# session，整个项目只执行一次
def login04():
    print("session")

