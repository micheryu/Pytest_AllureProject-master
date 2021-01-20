# coding = utf-8

"""

Author:micheryu
Date:2020/3/24
Motto: 能用脑，就别动手~
"""

import yaml
import os
import os.path


def parse():
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + r'\params\Params'
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r', encoding='utf-8')as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages


class GetPages:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = parse()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list()
    print(lists)
