# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: config_utils.py
# @time: 2020/7/5 11:50
# @desc
import configparser

class ConfigUtils:
    def __init__(self, config_path):
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path,encoding='utf-8')

    def read_value(self, section, key):
        value = self.conf.get(section,key)
        return value

