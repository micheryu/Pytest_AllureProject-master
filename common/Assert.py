# -*- coding : utf-8 -*-

"""
Name: Assert.py
Author: MicherYu
Date: 2020/3/25 10:42
Motto: 能用脑，就别动手~
"""

from log.logconf import logconf
from common import Consts
import json


class Assertions:
    def __init__(self):
        self.log = logconf()

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code: response.code
        :param expected_code: 预计code
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            self.log.error('StatusCode error,expected_code is {0},statusCode is {1}'.format(expected_code, code))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body: response.body
        :param dody_msg: response.text
        :param expected_msg: 预计msg
        :return:
        """

        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True
        except:
            self.log.error(
                'Response body msg != expected_msg, expected_msg is {0},body_msg is {1}'.format(expected_msg, body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response.body 中是否包含预期字符
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)

            assert expected_msg in text
            return True
        except:
            self.log.error('Response body Does not contain expected_msg,expected_msg is {0}'.format(expected_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response.body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """

        try:
            assert body == expected_msg
            return True
        except:
            self.log.error('Response body != expected_msg, expected_msg is {0}, body is {1}'.format(expected_msg, body))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_time(self, time, expected_time):
        """
        验证response.body响应时间小于预期最大响应时间，单位：毫秒
        :param time:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True
        except:
            self.log.error(
                'Response time > expected_time, expected_time is {0}, time is {1}'.format(expected_time, time))
            Consts.RESULT_LIST.append('fail')

            raise
