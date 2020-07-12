# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: jsonpat_demo.py
# @time: 2020/7/12 10:59
# @desc

import jsonpath
j = {'access_token': '35_l4G3zAPdtsCVjNTnGxhkUXsvmkll9cuM7h4WUid-XD0lvSLskNpf0ThpOp6Av9gTz5VGgiLkSA-0Z4YxGSG1zRIc4OHLMIkyFhht-Cge8HoSTAasexKCJVziPL--N_N7l32a79yY21NZcyh8KAZaAHAWML', 'expires_in': 7200}
print(jsonpath.jsonpath(j,'$.access_token')[0])