# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: config.py
# @time: 2020/7/5 11:54
# @desc

import os
from common.config_utils import ConfigUtils

current_path = os.path.dirname(__file__)
config_file = os.path.join(current_path, '..', 'conf/config.ini')

config_utils = ConfigUtils(config_file)
URL = config_utils.read_value('default', 'URL')
CASE_DATA_PATH = config_utils.read_value('path', 'CASE_DATA_PATH')

print(URL)
