import pytest


# @pytest.mark.parametrize("test_input,expected",
#                          [("1+3", 4),
#                           ("6*9", 54),
#                           ("2+4", 6)
#                           ])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected


# @pytest.mark.parametrize("x", [0, 1])
# @pytest.mark.parametrize("y", [2, 3])
# def test_foox(x, y):
#     print(f"测试数据组合：x->{x},y->{y}")
#

# @pytest.mark.parametrize("x", [0, 1,2])
# def test_foox(x):
#     print(f"测试数据组合：x->{x}")

@pytest.mark.parametrize("x,y", [(0,2),(1,3)])
def test_foox(x,y):
    print(f"测试数据组合：x->{x},y->{y}")


if __name__ == '__main__':
    pytest.main(["-s", "test_parametrize.py"])
