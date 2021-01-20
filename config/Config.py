# coding = utf-8

"""

Author:micheryu
Date:2020/3/24
Motto: 能用脑，就别动手~
"""

from configparser import ConfigParser
from log.logconf import logconf
import os


class Config:
    # titles
    TITLE_DEBUG = 'private_debug'
    # TITLE_RELEASE='online_release'
    TITLE_EMAIL = "mail"
    # values
    VALUE_TESTER = 'tester'
    VALUE_ENVIRONMENT = 'environment'
    VALUE_VERSION_CODE = 'versionCode'
    VALUE_HOST = 'host'
    VALUE_VERIFYCODEURL = 'verifyCodeUrl'
    VALUE_LOGINURL = 'loginUrl'

    # [mail]
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = logconf()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError('请确保配置文件存在！')
        self.config.read(self.conf_path, encoding='utf-8')

        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.verifyCodeUrl_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERIFYCODEURL)
        self.loginUrl_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGINURL)

        self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == '__main__':
    print(Config().get_conf('private_debug', 'host'))
