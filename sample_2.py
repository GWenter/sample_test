#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_2.py
# @Date    :2022/1/10 : 15:15

# 运算符

num_1 = 5
num_2 = 2

print("/:",end="")
print(num_1/num_2)

print("//:",end="")
print(num_1//num_2)

print("*:",end="")
print(num_1*num_2)

print("**:",end="")
print(num_1**num_2)


# 数据优先复用
str1 = "abc"
str2 = str("a+b+c")
print(str1 == str2)  # 比值大小
print(str1 is str2)  # 比id值，相当于内存地址
print(id(str1))
print(id(str2))
