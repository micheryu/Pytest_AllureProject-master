# coding = utf-8

"""

Author:micheryu
Date:2020/3/20
Motto: 能用脑，就别动手~
"""

from log.logconf import logconf
import allure, pytest, unittest


@allure.feature('测试搜索关键字')
class test_math(unittest.TestCase):
    def setUp(self, num1=4, num2=2):
        self.num1 = num1
        self.num2 = num2

    def tearDown(self):
        print('Finshed')

    def add(self):
        return self.num1 + self.num2

    @allure.story('测试加法')
    def test_add(self):
        logconf().info('计算{0}+{1}'.format(self.num1, self.num2))
        with allure.step('输入数字'):
            allure.attach('输入第一个数字:', '{0}'.format(self.num1))
            allure.attach('输入第二个数字:', '{0}'.format(self.num2))
            # logconf().error('错误：{0}+{1}'.format(num1,num2))
            assert self.add() == 6
    #
    # @allure.story('测试减法')
    # def test_jianfa(self):
    #     assert self.num1 - self.num2 == 2
    #
    # @allure.story('测试乘法')
    # def test_chengfa(self):
    #     assert self.num1 * self.num2 == 8
    #
    # @allure.story('测试出发')
    # def test_chufa(self):
    #     assert self.num1 / self.num2 == 2


if __name__ == '__main__':
    pytest.main(['-s', 'test_Add.py', '--alluredir',
                 r'D:\pycharm\PycharmProject\Study\Pytest_AllureProject\report\allure-report\test'])
