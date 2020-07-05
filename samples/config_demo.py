# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: config_demo.py
# @time: 2020/7/5 11:46
# @desc
import os
import configparser

current_path = os.path.dirname(__file__)
config_file = os.path.join(current_path, '..', 'conf/config.ini')
conf = configparser.ConfigParser()
conf.read(config_file,encoding='utf-8')
print(conf.get('path', 'CASE_DATA_PATH'))
