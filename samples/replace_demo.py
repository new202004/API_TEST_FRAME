# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: replace_demo.py
# @time: 2020/7/12 15:08
# @desc
import ast
import re

import requests

temp_varibles = {"token": "123456"}
parms = '{"access_token":${token}}'
value = re.findall('\\${\w+}', parms)[0]
print(value)

# parms = parms.replace(value, temp_varibles["token"])
parms = parms.replace(value, temp_varibles["token"])
print(parms)
# requests.get(url='',
#              parms=ast.literal_eval(parms))


temp_varibles = {"token": "123456", "number": "123", "age": "66"}
str = '"access_token":${token}，${age}==>${number}'
for v in re.findall('\\${\w+}', str):
    str = str.replace(v, temp_varibles.get(v[2:-1]))
print(str)
