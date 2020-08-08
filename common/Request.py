# -*- coding : utf-8 -*-

"""
Name: Request.py
Author: MicherYu
Date: 2020/3/25 15:17
Motto: 能用脑，就别动手~
"""

import requests
import os
import random
import common.Consts
from common import Seesion
from requests_toolbelt import MultipartEncoder
from Params import params


class Request:

    def __init__(self, env):
        """

        :param env:
        """
        self.session = Seesion.Session(env)
        self.get_session = self.session.get_session()
        # self.header_params = params.Basic().header[0]
        # print(self.header_params)
        self.header = {
            "Cookie": "SESSION=",
            "jwtToken": self.get_session
        }
        # self.header.update(self.header_params)
        # print(self.header)

    def get_request(self, url, data, header=params.Basic().header[0]):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        self.header.update(header)
        if not url.startswith('http://'):
            url = '{0}{1}'.format('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.get(url=url, headers=self.header)
            else:
                response = requests.get(url=url, json=data, headers=self.header)
        except requests.RequestException as e:
            print('{0}{1}'.format('RequestException url:', url))
            print(e)
            return ()
        except Exception as e:
            print('{0}{1}'.format('Exception url:', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        common.Consts.STRESS_LIST.append(time_consuming)
        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request(self, url, data, header=params.Basic().header[0]):
        """
        Post请求
        :param url:
        :param data:
        :param header:
        :return:
        """

        self.header.update(header)
        if not url.startswith('http://'):
            url = '{0}{1}'.format('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.post(url=url, headers=self.header)
            else:
                response = requests.post(url=url, json=data, headers=self.header)

        except requests.RequestException as e:
            print('{0}{1}'.format('RequestException url:', url))
            print(e)
            return ()
        except Exception as e:
            print('{0}{1}'.format('Exception url:', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request_multipart(self, url, data, file_parm, file, f_type, header=params.Basic().header[0]):
        """
        提交Multipart/form-data 格式的Post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param f_type:
        :return:
        """
        self.header.update(header)
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=self.header)
            else:
                data[file_parm] = os.path.basename(file), open(file, 'rb'), f_type

                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
                )

                self.header['Content-Type'] = enc.content_type
                response = requests.post(url=url, json=data, headers=self.header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        # time_consuming为响应时间，单位为毫秒
        time_consuming = response.elapsed.microseconds / 1000
        # time_total为响应时间，单位为秒
        time_total = response.elapsed.total_seconds()

        common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data, header=params.Basic().header[0]):
        """
        Put请求
        :param url:
        :param data:
        :param header:
        :return:

        """
        self.header.update(header)
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)

        try:
            if data is None:
                response = requests.put(url=url, headers=self.header)
            else:
                response = requests.put(url=url, json=data, headers=self.header)

        except requests.RequestException as e:
            print('%s%s' % ('RequestException url: ', url))
            print(e)
            return ()

        except Exception as e:
            print('%s%s' % ('Exception url: ', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds / 1000
        time_total = response.elapsed.total_seconds()

        common.Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts


if __name__ == '__main__':

    print(Request('debug').post_request('http://47.96.173.133:8080/pivot-ehr/task/approvesPage',{"pageNum":2,"pageSize":10,"cpo":{"queryParam":"","colorSign":[],"workflowType":[]},"employeeId":0,"endDate":"","startDate":""}))
