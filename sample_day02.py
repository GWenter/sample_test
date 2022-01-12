#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_day02.py
# @Date    :2022/1/11 : 9:37


#  作业


# # 数组转换
# list_1 = [[i, i+1, i+2] for i in range(1, 100, 3)]
# print(list_1)
#
# list_2 = [i for i in range(1, 101)]
# list_3 = [list_2[i:i+3] for i in range(0, len(list_2), 3)]
# print(list_3)


# # 九九乘法表
# def fun():
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print("%d*%d=%d" % (j, i, i * j), end=" ")
#         print("")
#
#
# fun()

# # 判断闰年还是平年
#
# def is_leap_year(year):
#     if year % 400 == 0:
#         print("yes")
#     elif year % 4 == 0 and year % 100 != 0:
#         print("yes")
#     else:
#         print("no")
#
#
# year = int(input())
# is_leap_year(year)


# # 打印1到100 的和
#
# def print_info():
#     num = 0
#     for i in range(1, 101):
#         num = num + i
#
#     print(num)
#
#
# print_info()
#

# # my_count
# def my_count():
#     num = 0
#     i = 2
#     while i <= 100:
#         if i % 2 == 0:
#             num = num + i
#
#         else:
#             num = num - i
#
#         i = i + 1
#     print(num)
#
#
# my_count()

# # get_level
# import random
#
#
# def get_level(score):
#     if 90 < score <= 100:
#         return 'A'
#     elif 80 < score <= 90:
#         return 'B'
#     else:
#         return 'C'
#
#
# for i in range(20):
#     stu = random.randint(0, 100)
#     print("成绩为%d,等级为%s" % (stu, get_level(stu)))
