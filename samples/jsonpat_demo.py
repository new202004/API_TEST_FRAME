# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: jsonpat_demo.py
# @time: 2020/7/12 10:59
# @desc
import re

import jsonpath

j = {
    'access_token': '35_l4G3zAPdtsCVjNTnGxhkUXsvmkll9cuM7h4WUid-XD0lvSLskNpf0ThpOp6Av9gTz5VGgiLkSA-0Z4YxGSG1zRIc4OHLMIkyFhht-Cge8HoSTAasexKCJVziPL--N_N7l32a79yY21NZcyh8KAZaAHAWML',
    'expires_in': 7200}
# print(jsonpath.jsonpath(j,'$.access_token')[0])


str = 'summer hot ~~'
pattern = re.compile(r"(\w+) (\w+)")
# print(re.sub(pattern, r"\2\1", str))
# print(re.sub(pattern, r"hello", str))
# print(str)

result = re.match(pattern, str)
print(result.group(1).title())


def fun(m):
    return m.group(1).title() + '' + m.group(2).title()


print(re.sub(pattern, fun, str))
