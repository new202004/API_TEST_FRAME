# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: read_excel01.py
# @time: 2020/7/5 9:22
# @desc

import os
import xlrd
from common.excel_utils import ExcelUtils

excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')
print(excel_path)
excel_utils = ExcelUtils(excel_path)
cell_value = excel_utils.get_merged_cell_value(4, 0)
print(cell_value)
#
# sheet_list = []
# for row in range(1, excel_utils.get_raw_count()):
#     row_dict = {}
#     row_dict["事件"] = excel_utils.get_merged_cell_value(row, 0)
#     row_dict["步骤"] = excel_utils.get_merged_cell_value(row, 1)
#     row_dict["步骤操作"] = excel_utils.get_merged_cell_value(row, 2)
#     row_dict["完成情况"] = excel_utils.get_merged_cell_value(row, 3)
#     sheet_list.append(row_dict)

all_data_list = []
first_row = excel_utils.sheet.row(0)
print(first_row)
for row in range(1, excel_utils.get_raw_count()):
    row_dict = {}
    for col in range(0, excel_utils.get_col_count()):
        row_dict[first_row[col].value] = excel_utils.get_merged_cell_value(row, col)
    all_data_list.append(row_dict)
print(all_data_list)