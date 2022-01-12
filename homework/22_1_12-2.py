#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : 22_1_12-2.py
# @Date    :2022/1/12 : 16:16


# 猜拳
import random

List = ('石头', '剪刀', '布')
Name = ('曹操', '张飞', '刘备')


class User(object):
    def __init__(self, name='', win=0, los=0, tie=0):
        self.name = name
        self.__win = win
        self.__los = los
        self.__tie = tie

    def add_win(self):
        self.__win += 1

    def add_los(self):
        self.__los += 1

    def add_tie(self):
        self.__tie += 1

    def get_win(self):
        return self.__win

    def get_los(self):
        return self.__los

    def get_tie(self):
        return self.__tie

    def game(self, num):
        print('=' * 20)
        print('玩家出拳，请输入序号： 1-石头  2-剪刀  3-布')
        try:
            k1 = int(input())
            print('=' * 20)
        except Exception:
            print('=' * 20)
            print("请输入序号：1-石头  2-剪刀  3-布")
        k2 = random.randint(1, 3)
        value_win = 0
        if k1 == 1:
            if k2 == 1:
                self.add_tie()
                value_win = 2
            elif k2 == 2:
                self.add_win()
                value_win = 0
            else:
                self.add_los()
                value_win = 1
        elif k1 == 2:
            if k2 == 1:
                self.add_los()
                value_win = 1
            elif k2 == 2:
                self.add_tie()
                value_win = 2
            else:
                self.add_win()
                value_win = 0
        else:
            if k2 == 1:
                self.add_win()
                value_win = 0
            elif k2 == 2:
                self.add_los()
                value_win = 1
            else:
                self.add_tie()
                value_win = 2
        print('电脑' + Name[num - 1] + '出的是' + List[k2 - 1])
        print('=' * 20)
        print('玩家%s出的是%s' % (self.name, List[k1 - 1]))
        if value_win == 0:
            print('玩家%s赢了此局' % self.name)
        elif value_win == 1:
            print('电脑%s赢了此局' % Name[num - 1])
        else:
            print('=' * 20)
            print('打平，再来300回合')


def main():
    print('=====欢迎参加石头剪刀布游戏=====')
    print('请输入玩家名称:')
    name = input()
    print('=' * 20)
    user = User(name)
    print('请选择电脑角色对应的序号： 1-曹操  2-张飞  3-刘备')
    try:
        num = int(input())
    except Exception:
        print('=' * 20)
        print('请选择电脑角色对应的序号： 1-曹操  2-张飞  3-刘备')
    flag = True
    while flag:
        flag2 = True
        user.game(num)
        print('=' * 20)
        print('是否继续游戏，继续输入y，退出游戏输入n：')
        while flag2:
            str = input()
            if str == 'n':
                flag = False
                flag2 = False
            elif str == 'y':
                flag2 = False
            else:
                print('=' * 20)
                print('是否继续游戏，继续输入y，退出游戏输入n：')
    print('玩家%s赢了%d局，平了%d局' % (user.name, user.get_win(), user.get_tie()))
    print('电脑%s赢了%d局，平了%d局' % (Name[num - 1], user.get_los(), user.get_tie()))
    print('游戏结束')
    print('=' * 20)


main()
