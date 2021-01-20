# coding = utf-8

"""

Author:micheryu
Date:2020/3/11
Motto: 能用脑，就别动手~
"""

import allure
import os
import pytest
import time
import unittest

# from selenium import webdriver
# from selenium.webdriver.common.by import By
from common.base import *
from log.logconf import logconf
from report.SendReport import SendReportEmail


# class GetDriver():
#     '''获取浏览器驱动'''
#
#     def __init__(self, browser_name):
#         self.driver = self.__get_driver(browser_name)
#
#     def __get_driver(self, browser_name):
#         __browser_name = browser_name.lower()
#         try:
#             if __browser_name.lower() == "chrome":
#                 __driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#             elif __browser_name.lower() == "firefox":
#                 __driver = webdriver.Firefox()
#             else:
#                 raise Exception("没有浏览器")
#         except Exception as e:
#             raise Exception("无法驱动浏览器")
#         else:
#             return __driver
#
#
# class BasePage():
#     '''页面基类'''
#
#     def __init__(self, driver):
#
#         self.driver = driver
#
#
#     def get(self, url):
#         try:
#             self.driver.get(url)
#         except:
#             raise Exception("打开%s 页面识别" % url)
#
#
#     def find_element(self, page_name, type, location):
#         try:
#             element = self.driver.find_element(type, location)
#         except:
#             raise Exception("没找到%s type=%s location=%s 这个元素" % (page_name, type, location))
#         else:
#             return element
#
#
# class HomePageResource():
#     ''' 首页页面资源信息 '''
#     input = {"page_name": "首页", "type": By.ID, "location": "input"}
#     click = {"page_name": "首页", "type": By.ID, "location": "search-button"}
#
#
# class HomePage(BasePage):
#     '''首页元素与操作'''
#
#     def input(self, page_name, type, location):
#         # input_element = self.find_element(**HomePageResource().input)
#         input_element = self.find_element(**{"page_name": page_name, "type": type, "location": location})
#         return input_element
#
#     def click(self, page_name, type, location):
#         # click_element = self.find_element(**HomePageResource().click)
#         click_element = self.find_element(**{"page_name": page_name, "type": type, "location": location})
#         return click_element
#


@allure.feature('测试搜索关键字')
class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver("chrome").driver
        cls.home_page = HomePage(cls.driver)
        logconf().info('初始化Chrome浏览器对象')

    @classmethod
    def tearDownClass(cls):
        logconf().info('测试结束，关闭浏览器')
        cls.driver.close()

    def setUp(self, url="http://www.so.com"):
        logconf().info('打开网页：{}'.format(url))
        self.home_page.get(url)

    def tearDown(self):
        logconf().info('浏览器休眠1s')
        time.sleep(1)
        # self.driver.close()
        pass

    @allure.story('搜索ABC')
    def testcase_01(self):
        with allure.step('搜索ABC'):
            allure.attach('输入框输入', 'abc')
            # self.home_page.input().send_keys('abc')
            logconf().info('执行输入关键字')
            self.home_page.input('首页', By.ID, 'input').send_keys("abc")
            allure.attach('点击按钮', '搜索')
            logconf().info('执行点击按钮')
            self.home_page.click('首页', By.ID, 'search-button').click()

    @allure.story('搜索python')
    def testcase_02(self):
        with allure.step('搜索python'):
            allure.attach('输入框输入', 'python')
            logconf().info('执行输入关键字')
            self.home_page.input('首页', By.ID, 'input').send_keys('python')
            allure.attach('点击按钮', '搜索')
            logconf().info('执行点击按钮')
            self.home_page.click('首页', By.ID, 'search-button').click()


if __name__ == '__main__':
    rootdir = os.getcwd()
    # print(rootdir)
    time = time.strftime('%Y-%m-%d_%H_%M_%S')
    rootpath = rootdir.replace(rootdir.split('\\')[-1], 'report') + r'\allure-report\{0}'.format(time)
    # print(rootpath)
    logconf('创建按时间生成测试报告文件夹')
    os.mkdir(rootpath)
    xmldir = rootpath + r'\xml'
    htmldir = rootpath + r'\html'
    os.mkdir(xmldir)
    os.mkdir(htmldir)
    logconf().info('执行pytest.main方法')
    pytest.main(['-s', 'test_search.py', '--alluredir', xmldir])
    logconf().info('美化测试报告')
    os.system('allure generate {0} -o {1} --clean'.format(xmldir, htmldir))

    SendReportEmail(rootdir.replace(rootdir.split('\\')[-1], 'report') + r'\allure-report').Find_File()
