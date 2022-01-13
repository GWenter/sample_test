#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : test_3.py
# @Date    :2022/1/13 : 10:56

# pickle

import pickle


def save(obj, file_path):
    with open(file_path, 'wb') as fd:
        pickle.dump(obj, fd)


def read(file_path):
    with open(file_path, 'rb') as fd2:
        result = pickle.load(fd2, encoding='utf-8')
        return result


list1 = ['zs', 'tom', 'linda']
path = '../data/pickle.obj'
save(list1, path)

obj = read(path)
print(obj)


