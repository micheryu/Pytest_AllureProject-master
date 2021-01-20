# -*- coding : utf-8 -*-

"""
Name: Shell.py
Author: MicherYu
Date: 2020/3/25 17:20
Motto: 能用脑，就别动手~
"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
