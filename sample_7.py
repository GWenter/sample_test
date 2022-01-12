#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_7.py
# @Date    :2022/1/12 : 9:13

# 类

# class A(object):
#     def fun(self):
#         print("--fun--")
#
#     def __str__(self):
#         return "--str--"
#
#     def __init__(self, name):
#         self.name = name
#
#
# a = A("zs")
# a.fun()
# print(a)
# print(a.name)
#

#
# class People(object):
#     name = 'zs'
#
# p1 = People()
# print(p1.name)
# p1.name = 'ls'
# print(p1.name)
#
# p2 = People()
# print(p2.name)


# class P(object):
#     name = 'zs'
#
#     @classmethod
#     def get_name(cls):
#         return P.name
#
#
# p1 = P()
# print(p1.get_name())


# class A(object):
#     def fun(self):
#         print("A")
#
#
# class B(object):
#     def fun(self):
#         print("B")
#
#
# class C(A, B):
#     def fun(self):
#         print("C")
#
#
# c = C()
#
# c.fun()


# class A(object):
#     # __name = 'zs'
#     # __age = 20
#
#     def __init__(self, name='zs', age=20):
#         self.__name = name
#         self.__age = age
#
#     # @classmethod
#     # def get_name(cls):
#     #     return cls.__name
#     #
#     # @classmethod
#     # def set_name(cls, name):
#     #     cls.__name = name
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
# a = A()
# print(a.get_name())
# print(a.get_age())


# class A(object):
#     __name = 'zs'
#
#     @classmethod
#     def get_name(cls):
#         return cls.__name
#
#
# print(A.get_name())
