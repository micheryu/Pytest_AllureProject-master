# -*- coding : utf-8 -*-

"""
Name: Seesion.py
Author: MicherYu
Date: 2020/3/25 11:27
Motto: 能用脑，就别动手~
"""

import requests

from log.logconf import logconf
from config import Config
from Params import params


class Session:
    def __init__(self, env):
        """
        :param env: 环境变量
        """
        self.config = Config.Config()
        self.log = logconf()
        self.param = params.Basic()
        self.env = env

    def get_code(self):
        """
        获取验证码换取jwtToken
        :return:
        """
        data = self.param.data[0]['phone']

        if self.env == 'debug':
            url = 'http://' + self.config.host_debug + self.config.verifyCodeUrl_debug + '{}'.format(data)
            # print(url)
            response = requests.post(url, json=data)

            if response.status_code == 200:
                # print(response.text)
                return response.status_code
            else:
                self.log.info('获取验证码失败：response.status_code={}'.format(response.status_code))
        elif self.env == 'release':
            print('Seesion.py&Config.py需配置release环境')
            pass

        else:
            self.log.error('get_code 环境配置参数有误！')

    def get_session(self):
        self.get_code()
        if self.env == 'debug':
            url = 'http://' + self.config.host_debug + self.config.loginUrl_debug
            parm = self.param.data[0]
            header = self.param.header[0]
            # session_debug=requests.session()
            # response=session_debug.post(url,parm,headers=header)
            response = requests.post(url, json=parm)
            # print(response.text)
            token = response.json()
            # print(token['data']['jwtToken'])
            return token['data']['jwtToken']
        elif self.env == 'release':
            print('Session.py&Config.py需配置release环境')
            pass
        else:
            self.log.error('环境配置参数有误！')


if __name__ == '__main__':
    Session('debug').get_session()
