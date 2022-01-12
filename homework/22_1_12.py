#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : 22_1_12.py
# @Date    :2022/1/12 : 15:38


# animals+dog+cat
class Animals(object):
    '''
    __name
    __legs
    '''

    def __init__(self, name='animals', legs=0):
        self.__name = name
        self.__legs = legs

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_legs(self, legs):
        self.__legs = legs

    def get_legs(self):
        return self.__legs


class Cat(Animals):
    '''
    __name
    __legs
    __age
    __price
    '''

    def __init__(self, name='cat', age=0, price=0.0, legs=0):
        self.set_name(name)
        self.set_legs(legs)
        self.__age = age
        self.__price = price

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def shout(self):
        print("---喵---")

    def eat(self):
        print("---eat mouse---")


class Dog(Animals):
    '''
    __name
    __legs
    __age
    __price
    '''

    def __init__(self, name='dog', age=0, price=0.0, legs=0):
        self.set_name(name)
        self.set_legs(legs)
        self.__age = age
        self.__price = price

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def shout(self):
        print("---汪---")

    def eat(self):
        print("---eat meat---")


animals = Animals(name='animals', legs=4)

Bos_cat = Cat(name='bos', age=2, price=200, legs=4)

Bali_cat = Cat(name='bali', age=1, price=300, legs=4)

Spi_dog = Dog(name='spi', age=1, price=250, legs=3)

Dot_dog = Dog(name='dot', age=3, price=350, legs=4)

print(Bos_cat.get_name())
Bos_cat.shout()






