# coding = utf-8

"""

Author:micheryu
Date:2020/3/20
Motto: 能用脑，就别动手~
"""

import logging
import logging.config
import yaml, os


# def create_file(filename):
#     path = filename[0:filename.rfind('/')]
#     print(path)
#     if not os.path.isdir(path):
#         os.mkdir(path)
#     if not os.path.isfile(filename):
#         fd = open(filename, mode='w', encoding='utf-8')
#         fd.close()
#
#     else:
#         pass


# 执行testcases/Run.py
def logconf(path='logging.yml'):
    config_file = os.path.join(os.path.dirname(__file__), path)

    # print(config_file)
    config_file = config_file.replace('\\', '/')
    # print(config_file)
    if os.path.exists("{0}/mylog".format(os.path.dirname(__file__))):
        pass
    else:
        os.mkdir("{0}/mylog".format(os.path.dirname(__file__)))
    with open(config_file, 'rt')as f_conf:
        dict_conf = yaml.unsafe_load(f_conf)
    logging.config.dictConfig(dict_conf)
    logger = logging.getLogger('simpleExample')

    return logger


#  执行根目录run.py  需将logging.yml log配置路径改为log/mylog/info.log
# def logconf(path=r'log\logging.yml'):
#     config_file = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     config_file = os.path.join(config_file, path)
#
#     # print(config_file)
#     # config_file = config_file.replace('\\', '/')
#     # print(config_file)
#     with open(config_file, 'rt')as f_conf:
#         dict_conf = yaml.unsafe_load(f_conf)
#         # print(type(dict_conf),dict_conf)
#     logging.config.dictConfig(dict_conf)
#     logger = logging.getLogger('simpleExample')
#
#     return logger


if __name__ == '__main__':
    logconf()
