# coding = utf-8

"""

Author:micheryu
Date:2020/3/20
Motto: 能用脑，就别动手~
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class GetDriver():
    '''获取浏览器驱动'''

    def __init__(self, browser_name):
        self.driver = self.__get_driver(browser_name)

    def __get_driver(self, browser_name='chrome',
                     driverpath=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'):
        __browser_name = browser_name.lower()
        try:
            if __browser_name.lower() == "chrome":
                __driver = webdriver.Chrome(driverpath)
            elif __browser_name.lower() == "firefox":
                __driver = webdriver.Firefox()
            else:
                raise Exception("没有浏览器")
        except Exception as e:
            raise Exception("无法驱动浏览器")
        else:
            return __driver

#
# if __name__ == '__main__':
#     GetDriver('chrome')


class BasePage():
    '''页面基类'''

    def __init__(self, driver):

        self.driver = driver

    def get(self, url):
        try:
            self.driver.get(url)
        except:
            raise Exception("打开%s 页面识别有误" % url)

    def find_element(self, page_name, type, location):
        try:
            element = self.driver.find_element(type, location)
        except:
            raise Exception("没找到%s type=%s location=%s 这个元素" % (page_name, type, location))
        else:
            return element


class HomePage(BasePage):
    '''首页元素与操作'''

    def input(self, page_name, type, location):
        # input_element = self.find_element(**HomePageResource().input)
        input_element = self.find_element(**{"page_name": page_name, "type": type, "location": location})
        return input_element

    def click(self, page_name, type, location):
        # click_element = self.find_element(**HomePageResource().click)
        click_element = self.find_element(**{"page_name": page_name, "type": type, "location": location})
        return click_element

