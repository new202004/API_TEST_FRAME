# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: localconfig_utils.py
# @time: 2020/7/5 11:59
# @desc

import configparser

class ConfigUtils:
    def __init__(self, config_path):
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path,encoding='utf-8')

    def read_value(self, section, key):
        value = self.conf.get(section,key)
        return value

    def url(self):
        url_value = self.read_value('default', 'URL')
        return url_value

    def case_data_path(self):
        case_data_path = self.read_value('path', 'CASE_DATA_PATH')
        return case_data_path

if __name__ == '__main__':
    import os
    current_path = os.path.dirname(__file__)
    config_file = os.path.join(current_path, '..', 'conf/config.ini')
    url = ConfigUtils(config_file).url()
    print(url)
