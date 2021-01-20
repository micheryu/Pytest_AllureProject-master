# coding = utf-8

"""

Author:micheryu
Date:2020/3/24
Motto: 能用脑，就别动手~
"""

import os

from log.logconf import logconf
from Params import tools

log = logconf()

path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


# print(path_dir)


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class Basic:
    log.info('解析yaml,Path: ' + path_dir + r'/Params/Params/Basic.yml')
    params = get_parameter('Basic')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        # url.append(params[i]['loginUrl'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
    # print(url, data, header)


class ApprovesPage:
    log.info('解析yaml,path: ' + path_dir + r'/Params/Params/approvesPage.yml')
    params = get_parameter('approvesPage')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        # url.append(params[i]['loginUrl'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
    # print(url, data, header)


if __name__ == '__main__':
    ApprovesPage()
