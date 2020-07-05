# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: testdata_utils.py
# @time: 2020/7/5 11:03
# @desc
import os
from common.excel_utils import ExcelUtils

current_path = os.path.dirname(__file__)
test_data_file = os.path.join(current_path, '..', 'test_data/weixin_data.xlsx')


class TestdataUtils:
    def __init__(self, test_data_path=test_data_file):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtils(test_data_file, "Sheet1").get_sheet_data_by_dict()

    def get_testcase_data_dict(self):
        case_dict = {}
        for row_data in self.test_data:
            case_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return case_dict

    def get_testcase_data_list(self):
        test_case_list = []
        for k, v in self.get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict['case_name'] = k
            one_case_dict['case_info'] = v
            test_case_list.append(one_case_dict)
        return test_case_list


if __name__ == '__main__':
    test_data_utils = TestdataUtils()
    # data_info = test_data_utils.get_testcase_data()
    data_info = test_data_utils.get_testcase_data_list()
    print(data_info)
