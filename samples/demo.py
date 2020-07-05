# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: demo.py
# @time: 2020/7/5 10:42
# @desc

a = {'one': [1], 'two': 2, 'three': 3}
a.setdefault('four', 4)  # 不存在，新增，存在，修改
a.setdefault('one', 4)  # 不存在，新增，存在，不修改
# print(a)
a.setdefault('five', []).append('5')
a.append('1')
print(a)


a = {'one': 1, 'two': 1, 'three': 3}
a1 = {'one': 1, 'two': 2, 'three': 3}

b = {'one': 2, 'two': 2, 'three': 3}
c = {'one': 3, 'two': 2, 'three': 3}

list_a = [{'测试用例编号': 'case01', '测试用例名称': '测试能否正常执行获取token接口', '用例执行': '是', '测试用例步骤': 'step_01'},
          {'测试用例编号': 'case02', '测试用例名称': '测试能否正常新增用户标签', '用例执行': '是', '测试用例步骤': 'step_01'},
          {'测试用例编号': 'case02', '测试用例名称': '测试能否正常新增用户标签', '用例执行': '是', '测试用例步骤': 'step_02'},
          {'测试用例编号': 'case03', '测试用例名称': '测试能否正常删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01'},
          {'测试用例编号': 'case03', '测试用例名称': '测试能否正常删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02'}]

case_list = {}
for i in list_a:
    case_list.setdefault(i['测试用例编号'], []).append(i)


# all_case_list = []
# for i in list_a:
#     all_case = {}
#     case_list.setdefault(i['测试用例编号'], []).append(i)
#     all_case["case_name"] = i['测试用例编号']
#     all_case["case_info"] = case_list[i['测试用例编号']]
#     all_case_list.append(all_case)
# print(all_case)

# print(case_list)

#
# case_dict = {}
# for i in list_a:
#     case_dict.setdefault(i['测试用例编号'], []).append(i)
# print(case_dict)
#
# case_list = []
# for k,v in case_dict.items():
#     case_dict_ = {}
#     case_dict['case_name'] = k
#     case_dict['case_info'] = v
#     case_list.append(case_dict)
#
# for c in case_list:
#    print(c)