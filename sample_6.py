#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_6.py
# @Date    :2022/1/11 : 16:22

# 匿名函数

# num1 = 1
# num2 = 2


#
# def add(x, y):
#     return x + y


# # 匿名函数
# add_lbd = lambda x, y: x + y  # 取名为add_lbd
# print(add_lbd(num1, num2))


# # 匿名用法
# def fun(x, y, fun_):
#     print(fun_(x, y))
#
#
# fun(num1, num2, lambda x, y: x + y)


# 值的调用
def fun1():
    num1 = 100
    num4 = 600

    def fun2():
        nonlocal num1
        num1 = 200
        num2 = 100

        def fun3():
            nonlocal num1
            nonlocal num2
            nonlocal num4
            num1 = 300
            num2 = 200
            num3 = 100
            num4 = 700
            print("fun3_num1:", num1)
            print("fun3_num2:", num2)
            print("fun3_num3:", num3)
            print("fun3_num4:", num4)

        fun3()
        print("fun2_num1:", num1)
        print("fun2_num2:", num2)

    fun2()
    print("fun1_num1:", num1)
    print("fun1_num4:", num4)


fun1()
