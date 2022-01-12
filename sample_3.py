#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_3.py
# @Date    :2022/1/10 : 15:39

# 条件结构，循环结构，判断

age = 7
if age < 6:
    print("age<6")
else:
    print("age>=6")

if age < 6:
    print("age<6")
elif age < 9:
    print("6<=age<9")
else:
    print("age>=9")

# range(a,b,c) a其实，b尾不计入，c间隔相当于i+=c，默认为1
sum = 0
for i in range(1,101):
    sum = sum + i
print(sum)


sum_1 = int(input())
sum_2 = int(input())
num = 0
if sum_1>sum_2:
    for i in range(sum_2,sum_1):
        num += i
else:
    for i in range(sum_1,sum_2):
        num += i

print(num)


def fun():
    pass   # pass跳过防报错   #TODO