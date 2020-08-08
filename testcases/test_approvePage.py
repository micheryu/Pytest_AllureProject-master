# -*- coding : utf-8 -*-

"""
Name: test_approvePage.py
Author: MicherYu
Date: 2020/3/26 15:41
Motto: 能用脑，就别动手~
"""

import allure

import pytest

from Params.params import ApprovesPage
from config import Config
from common import Request
from common import Consts
from common import Assert


class Test_login:

    @pytest.allure.feature('待审批列表')
    @allure.severity('blocker')
    @allure.story('待我审批')
    def test_login_01(self, action):
        """
        测试获取登陆状态
        :param action:
        :return:
        """
        conf = Config.Config()
        data = ApprovesPage()
        test = Assert.Assertions()
        request = Request.Request(action)
        urls = data.url
        params = data.data
        host = conf.host_debug
        req_url = 'http://' + host
        headers = data.header

        api_url = req_url + urls[0]['approvers_list']
        # print(api_url, urls, params)
        response = request.post_request(api_url, params[0], headers[0])
        # print(response)
        with allure.step('校验结果'):
            allure.attach('校验返回code', '预期code：{0}，实际code：{1}'.format(response['code'], 200))
            assert test.assert_code(response['code'], 200)
            allure.attach('校验返回message', '预期msg：{0}，实际msg：{1}'.format(response['body']['errorMessage'], '成功'))
            assert test.assert_text(response['body']['errorMessage'], '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == '__main__':
    Test_login()
