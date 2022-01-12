#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_5.py
# @Date    :2022/1/11 : 10:32


# 递归

def fun(max):
    a = 1
    b = 1
    i = 0
    while i < max:
        yield b
        a, b = b, a + b
        i = i + 1


for n in fun(5):
    print(n)

