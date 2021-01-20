# coding = utf-8

"""

Author:micheryu
Date:2020/3/23
Motto: 能用脑，就别动手~
"""
import os
import time

import pytest

from common import Shell
from config import Config
from log import logconf
from report import SendReport


def run(time_str):
    conf = Config.Config()
    log = logconf.logconf()
    log.info('初始化配置文件，path= ' + conf.conf_path)
    shell = Shell.Shell()
    root_dir = os.getcwd()
    # print(root_dir)
    root_path = root_dir.replace(root_dir.split('\\')[-1], 'report') + r'\allure-report\{0}'.format(time_str)
    # print(root_path)
    log.info('创建按时间生成测试报告文件夹')
    os.mkdir(root_path)
    xml_dir = root_path + r'\xml'
    html_dir = root_path + r'\html'
    os.mkdir(xml_dir)
    os.mkdir(html_dir)
    # args = ['-s', '-q', '--alluredir', xmldir]
    args = ['-s', 'test_search.py', '--alluredir', xml_dir]
    pytest.main(args)
    cmd = 'allure generate {0} -o {1} --clean'.format(xml_dir, html_dir)
    # os.system('allure generate {0} -o {1} --clean'.format(xmldir, htmldir))

    # print(rootdir)
    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行测试用例失败，请检查环境配置')
        raise

    try:
        mail = SendReport.SendReportEmail(root_dir.replace(root_dir.split('\\')[-1], 'report') + r'\allure-report')
        mail.Find_File()
    except Exception as e:
        log.error('发送邮件失败，请检查邮件配置')
        raise


if __name__ == '__main__':
    time = time.strftime('%Y-%m-%d_%H_%M_%S')

    run(time)
