# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: exception_demo.py
# @time: 2020/7/19 9:40
# @desc

import requests
from requests.exceptions import RequestException

res = requests.get(url='http://google.com.hk/')
print('!!!!!!!!!!!!!!!!!!!!!!!!1', res.status_code)
