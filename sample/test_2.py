#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : test_2.py
# @Date    :2022/1/13 : 8:55



# file . oi

#
# file_open = open(r"../data/a.txt", encoding='utf-8')
#
# str_fo = file_open.read(1)    #h
# str_1 = file_open.readline()  #ello world
# str_2 = file_open.readlines()
#
# print(str_fo)
# print(str_1)
# print(str_2)
#
# file_open.close()


file_w = open(r"../data/a.txt", mode="w")
file_w.write("new world")
file_w.close()


# 出现异常时自动close对象
with open("../data/a.txt",'r',encoding='utf-8') as fo_1:
    print(fo_1.read())

