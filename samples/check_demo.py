# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: check_demo.py
# @time: 2020/7/12 17:03
# @desc

# 正则匹配测试

# 实际结果
import ast
import re

str1 = '{"access_token":"35_d3hHqXMhprg5WHxJmnJQeidqjc5iCw' \
       '-OgdeN46wAU8Yet79Tk1wn5U10kwaYSgxRZC7p3Nxfo7hEgN5tVXfH9vvTfC1tJkUYAxFdeY3tZJiW9m1DiXlOPCLI4I_nMptXgozyn4FHZfp29DgfBSKiADASJB"}'

# 期望结果
str2 = '{"access_token":"(.+?)"}'

if re.findall(str2, str1):
    print(True)
else:
    print(False)

# 是否包含json key
json_data = ast.literal_eval(str1)
str2 = 'access_token'

print(str2 in json_data.keys())
