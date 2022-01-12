#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_1.py
# @Date    :2022/1/10 : 14:51

# test input and output

value_1 = "hello"
print(value_1)

value_2 = "world"
print(value_1,end="")
# print自动回车,end=""取消回车
print(value_2,end="\n")
print("1")

value_3 = input()
print(value_3)
print(type(value_3))
# 默认input为str
