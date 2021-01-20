# coding = gbk


import allure
import pytest



def test_01():
    """
    用例描述：Test case 01
    :return: True or False
    """
    x = "this"
    assert 'h' in x


def test_02():
    x = "hello"
    assert 'x' in x



def add(a, b):
    """
    用例描述：Test case 02
    :return: True or False
    """
    return a + b


# 测试Test case 02结果
def test_add():
    """
    用例描述：测试add（）返回结果是否一致
    :return:
    """
    assert add(1, 1) == 2



#
# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', './allure-results'])
