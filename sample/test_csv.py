#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : test_csv.py
# @Date    :2022/1/13 : 11:11


# csv

import csv

path = '../data/test.csv'


#
# def write_csv(content, file_path):
#     """
#     xieru csv
#     :param content:  xieru neirong
#     :param file_path:
#     :return:
#     """
#
#     with open(file_path, 'a', encoding='utf-8', newline='') as fd:
#         writer = csv.writer(fd)
#         # writer.writerow(content)
#         writer.writerows(content)
#

#
# if __name__ == '__main__':
#     title_list = ['csmc', 'qt', 'qiwen', 'qiya']
#     data_list = ['wh', 'qing', 'liang', '30']
#     # write_csv(title_list, path)
#     write_csv([title_list, data_list], path)

def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as rd:
        reader = csv.reader(rd)
        print(type(reader))
        for item in reader:
            print(item)


if __name__ == '__main__':
    read_csv(path)
