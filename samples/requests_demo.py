# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: requests_demo.py
# @time: 2020/7/5 14:57
# @desc

import requests

hosts = 'https://api.weixin.qq.com/'


# 获取token
def test_token():
    url = 'cgi-bin/token'
    get_data = {'grant_type': 'client_credential', 'appid': 'wx92a26fcb387a96f4',
                'secret': '7df85a6d63862066bc8477fe12dfe6ad'}
    response = requests.get(url=hosts + url, params=get_data).json()
    token = response['access_token']
    return token


# 创建一个标签
def create_tag(token):
    get_params = {"access_token": token}
    # post_params = {"tag": {"name": "长沙009"}}
    post_params = {'tag': {'name': '7月8888'}}
    headers = {"content_type": "applocation/json"}
    response = requests.post(url=hosts + 'cgi-bin/tags/create',
                             params=get_params,
                             json=post_params,
                             headers=headers).json()
    print(get_params)


if __name__ == '__main__':
    token = test_token()
    print(token)
    create_tag(token)
