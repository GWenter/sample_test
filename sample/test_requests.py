#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : test_requests.py
# @Date    :2022/1/13 : 15:25


# requests
import csv
import json

import requests as req

#
# url = "https://duanzixing.com/"
# resp = req.get(url)
# print(type(resp))
#
# print(resp.content.decode('utf-8'))


# 登录人人网
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
data = {

}
file_path = '../data/data.txt'
data = json.dumps(data)
url_bili = 'https://www.bilibili.com/v/popular/rank/all'

resp = req.get(url_bili)
print(resp.content.decode('utf-8'))
# str = resp.content.decode('utf-8')
# # print(type(str))
# try:
#     write = open(file_path, 'w')
#     write.write(str)
# except Exception:
#     print("open error")
# finally:
#     write.close()
# with open(file_path, 'r', encoding='utf-8', newline='') as rf:
#     reader = csv.reader(rf)
#     print(reader)
