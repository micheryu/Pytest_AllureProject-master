# -*- coding : utf-8 -*-

"""
Name: conftest.py
Author: MicherYu
Date: 2020/3/26 16:10
Motto: 能用脑，就别动手~
"""
import pytest
import allure

from config.Config import Config
from common import Consts


@pytest.fixture()
def action():
    # 定义环境
    env = Consts.API_ENVIRONMENT_DEBUG
    conf = Config()
    host = conf.host_debug
    tester = conf.tester_debug
    allure.environment(environment=env)
    allure.environment(hostname=host)
    allure.environment(tester=tester)
    return env
