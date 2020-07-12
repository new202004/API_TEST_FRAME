# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: requets_utils.py
# @time: 2020/7/12 8:50
# @desc
import ast

import requests
from common.localconfig_utils import config


class RequetsUtils:
    def __init__(self):
        self.hosts = config.url()
        self.headers = {"Content-Type": "application/json"}
        self.session = requests.session()

    def get(self, get_info):
        url = self.hosts + get_info["请求地址"]
        param = ast.literal_eval(get_info["请求参数(get)"])  # 将字典转换为字符串
        res = self.session.get(url=url, params=param)
        res.encoding = res.apparent_encoding

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

        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': res.reason,
            'response_code': res.status_code,
            'response_headers': res.headers,
            'response_body': res.json()
        }
        return result


if __name__ == '__main__':
    get_info = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01',
                '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token',
                '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}',
                '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在',
                '期望结果': 'access_token,expires_in'}
    post_info = {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口',
                 '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}',
                 '提交数据（post）': '{"tag":{"id":23}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对',
                 '期望结果': '{"errcode":0,"errmsg":"ok"}'}
    re = RequetsUtils()
    # response = re.get(get_info)
    response = re.post(post_info)
    print(response)
