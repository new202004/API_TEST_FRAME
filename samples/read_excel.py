# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: read_excel.py
# @time: 2020/7/1 21:14
# @desc
import os
import xlrd

excel_path = os.path.join(os.path.dirname(__file__), 'data/test_data.xlsx')
print(excel_path)

wb = xlrd.open_workbook(excel_path)
sheet = wb.sheet_by_name("Sheet1")
cell_value = sheet.cell_value(0, 0)  # 对于合并的单元格首个单元格会返回真实值


# print(cell_value)

# 处理方式：xlrd
# print(sheet.merged_cells)  # 返回一个列表  起始行，结束行，起始列，结束列


# 逻辑 凡是在merged_cells属性范围内的单元格 它的值都要等于左上角首页单元格的值

def get_merged_cell_value(row_index, col_index):
    """既能获取合并单元格的数据，又能获取合并单元格的数据"""
    merged = sheet.merged_cells
    print(merged)
    sheet_value = None
    for (rlow, rhigh, clow, chigh) in merged:
        if rlow <= row_index < rhigh:
            if clow <= col_index < chigh:
                sheet_value = sheet.cell_value(rlow, clow)
                break;  # 防止循环取进行判断出现值覆盖的情况
            else:
                sheet_value = sheet.cell_value(row_index, col_index)
        else:
            sheet_value = sheet.cell_value(row_index, col_index)
    return sheet_value


if __name__ == '__main__':
    value = get_merged_cell_value(1, 0)
    print(value)
