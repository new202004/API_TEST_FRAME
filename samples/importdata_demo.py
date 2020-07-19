# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: importdata_demo.py
# @time: 2020/7/19 9:27
# @desc

# 使用excel中的数据去驱动 requests_utils

from common.testdata_utils import TestdataUtils
from common.requets_utils import RequetsUtils

test_data_utils = TestdataUtils()
all_case_info = test_data_utils.get_testcase_data_list()

for case_info in all_case_info:
    case_info = case_info.get('case_info')
    res = RequetsUtils()
    result = res.requets_by_step(case_info)
    print(result)
