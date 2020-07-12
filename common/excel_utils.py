# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: excel_utils.py
# @time: 2020/7/5 8:57
# @desc

import os
import xlrd


class ExcelUtils:
    def __init__(self, file_path, sheet_name='Sheet1'):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.sheet = self.get_sheet()  # 整个表格对象

    # 通过文件名称读取数据
    def get_sheet(self):
        wb = xlrd.open_workbook(self.file_path)
        sheet = wb.sheet_by_name(self.sheet_name)
        return sheet

    # 获取行的总数
    def get_raw_count(self):
        row_count = self.sheet.nrows
        return row_count

    # 获取列的总数
    def get_col_count(self):
        col_count = self.sheet.ncols
        return col_count

    # 获取根据行列单个数据
    def get_cell_value(self, row_index, col_index):
        c_value = self.sheet.cell_value(row_index, col_index)
        return c_value

    # 获取所有合并单元格的行列宽高
    def get_merged_info(self):
        merged_info = self.sheet.merged_cells
        return merged_info

    # 获取单元格的数据（包含合并与正常）
    def get_merged_cell_value(self, row_index, col_index):
        """既能获取合并单元格的数据，又能获取合并单元格的数据"""
        sheet_value = None
        if self.get_merged_info():
            for (rlow, rhigh, clow, chigh) in self.get_merged_info():
                if rlow <= row_index < rhigh:
                    if clow <= col_index < chigh:
                        sheet_value = self.get_cell_value(rlow, clow)
                        break;  # 防止循环取进行判断出现值覆盖的情况
                    else:
                        sheet_value = self.get_cell_value(row_index, col_index)
                else:
                    sheet_value = self.get_cell_value(row_index, col_index)
        else:
            sheet_value = self.get_cell_value(row_index, col_index)
        return sheet_value

    # 获取所有数据，字典格式
    def get_sheet_data_by_dict(self):
        all_data_dict = []
        first_row = self.sheet.row(0)
        # print(first_row)
        for row in range(1, self.get_raw_count()):
            row_dict = {}
            for col in range(0, self.get_col_count()):
                row_dict[first_row[col].value] = self.get_merged_cell_value(row, col)
            all_data_dict.append(row_dict)
        return all_data_dict




if __name__ == '__main__':
    excel_path = os.path.join(os.path.dirname(__file__), '../test_data/test_case.xlsx')
    print(excel_path)
    excel_utils = ExcelUtils(excel_path)
    cell_value = excel_utils.get_merged_cell_value(1, 0)
    # print(cell_value)
    for i in excel_utils.get_sheet_data_by_dict():
        print(i)
        print('\n')
