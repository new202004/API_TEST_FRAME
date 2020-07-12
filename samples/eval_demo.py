# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: eval_demo.py
# @time: 2020/7/12 9:12
# @desc


print(eval("{'a':'a'}"))  # 将字符串转化为字典
print(eval("{'a': age}", {"age": 18}))  # 传递变量
