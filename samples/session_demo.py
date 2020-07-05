# !/usr/bin/env python
# encoding: utf-8
# @author: new

import requests
import re
from collections import OrderedDict

php_url = 'http://47.107.178.45/phpwind/index.php'
user_name = 'new001'
password = '123456'
title = 'titlenew0011'
content = 'contentnew0011'


def get_token(seesion):
    body = seesion.get(php_url).text
    token = re.findall("TOKEN : '(.+?)'", body)[0]
    return token


def login(session_req, token):
    header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
              'X-Requested-With': 'XMLHttpRequest',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Accept-Encoding': 'gzip, deflate',
              'Accept-Language': 'zh-CN,zh;q=0.8'}

    get_data = {'m': 'u', 'c': 'login', 'a': 'dorun'}
    post_data = {'username': user_name, 'password': password, 'csrf_token': token}
    response = session_req.post(php_url, params=get_data, data=post_data, headers=header)
    content = response.text
    status = re.findall("&_statu=(.+?)\"", content)[0]
    print(status)
    return status


def login_after(status, session):
    get_data = {'m': 'u', 'c': 'login', 'a': 'welcome', '_statu': status}
    response = session.get(php_url, params=get_data)


def post(token, session):
    # header = {'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryKQVxS4TACFKqIQzh'}

    get_data = {'c': 'post', 'a': 'doadd', '_json': '1', 'fid': '83'}
    post_data = OrderedDict([("atc_title", (None, title)),
                             ("atc_content", (None, content)),
                             ("pid", (None, '')),
                             ("tid", (None, '')),
                             ("special", (None, 'default')),
                             ("reply_notice", (None, '1')),
                             ("csrf_token", (None, token))])
    response = session.post(php_url, params=get_data, files=post_data).json()
    print(response)


if __name__ == '__main__':
    session_req = requests.session()  # 用session保持对话连接
    token = get_token(session_req)
    status = login(session_req, token)
    login_after(status, session_req)
    post(token, session_req)