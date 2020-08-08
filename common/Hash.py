# -*- coding : utf-8 -*-

"""
Name: Hash.py
Author: MicherYu
Date: 2020/3/27 10:19
Motto: 能用脑，就别动手~
"""

from hashlib import sha1
from hashlib import md5


def my_md5(msg):
    """
    md5 加密
    :param msg: 需加密的字符串
    :return: 加密后的字符串
    """
    h1 = md5()
    h1.update(msg.encode('utf-8'))
    return h1.hexdigest()


def my_sha1(msg):
    """
    sha1 加密
    :param msg: 需加密的字符串
    :return: 加密后的字符
    """
    sh = sha1()
    sh.update(msg.encode('utf-8'))
    return sh.hexdigest()


if __name__ == '__main__':
    print(my_md5('测试'))
    print(my_sha1('测试'))