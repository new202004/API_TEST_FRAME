# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: requets_utils.py
# @time: 2020/7/12 8:50
# @desc
import ast

import requests
import jsonpath
from common.localconfig_utils import config


class RequetsUtils:
    def __init__(self):
        self.hosts = config.url()
        self.headers = {"Content-Type": "application/json"}
        self.session = requests.session()
        self.temp_varibles = {}  # 临时变量，存放动参

    def get(self, get_info):
        url = self.hosts + get_info["请求地址"]
        param = ast.literal_eval(get_info["请求参数(get)"])  # 将字典转换为字符串
        res = self.session.get(url=url, params=param)
        res.encoding = res.apparent_encoding

        if get_info["取值方式"] == "json取值":
            value = jsonpath.jsonpath(res.json(), get_info["取值代码"])
            self.temp_varibles[get_info["传值变量"]] = value
        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': res.reason,
            'response_code': res.status_code,
            'response_headers': res.headers,
            'response_body': res.json()
        }
        return result

    def post(self, post_info):
        url = self.hosts + post_info["请求地址"]
        # param = ast.literal_eval(post_info["请求参数(get)"])  # 将字典转换为字符串

        param = {
            "access_token": '35_6PGm9X9-2UocsAF10yP0NuheTdGTbOWP07etOPveJAHCD-YBcN_vURPNz_PY0JQb6EULIBYWDF_iXcv2MxKzOdnjIU3pzmj0y6Tjes15xyOCbR3BResSwYETBiu0iGtTFAcG2UIApbFnIQtSYILiAJALVY'}
        data = ast.literal_eval(post_info["提交数据（post）"])
        res = self.session.post(url=url, params=param, data=data)
        res.encoding = res.apparent_encoding
        if post_info["取值方式"] == "json取值":
            value = jsonpath.jsonpath(res.json(), post_info["取值代码"])
            self.temp_varibles[post_info["传值变量"]] = value
        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': res.reason,
            'response_code': res.status_code,
            'response_headers': res.headers,
            'response_body': res.json()
        }
        return result

    def request(self, step_info):
        request_type = step_info["请求方式"]
        if request_type == "get":
            result = self.get(step_info)
        elif request_type == "post":
            result = self.post(step_info)
        else:
            result = {'code': 3, 'result': '请求方式不支持'}
        print(result['response_body'])
        return result

    # 同一个接口多个步骤封装实现
    def requets_by_step(self, step_infos):
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result['code'] != 0:
                break
            else:
                result = temp_result
        return result


if __name__ == '__main__':
    # get_info = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01',
    #             '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token',
    #             '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
    #             '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在',
    #             '期望结果': 'access_token,expires_in'}
    # post_info = {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口',
    #              '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}',
    #              '提交数据（post）': '{"tag":{"id":23}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对',
    #              '期望结果': '{"errcode":0,"errmsg":"ok"}'}
    # response = re.request(post_info)

    case_info = {'case_name': 'case02', 'case_info': [
        {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口',
         '请求方式': 'get', '请求地址': '/cgi-bin/token',
         '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
         '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配',
         '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'},
        {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口',
         '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}',
         '提交数据（post）': '{"tag" : {"name" : "衡东8888"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': '正则匹配',
         '期望结果': '{"tag":{"id":(.+?),"name":"衡东8888"}}'}]}
    re = RequetsUtils()
    step_infos = case_info["case_info"]
    result = re.requets_by_step(step_infos)
    print(result)
