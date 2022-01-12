#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_8.py
# @Date    :2022/1/12 : 14:05

# 异常
#
# try:
#     a = 1
# except Exception:
#     print("Exception")
#
# try:
#     print(a)
#     print("**")
# except Exception:
#     print("NONE value")
#
# print("--")


# import traceback  # 跟踪异常
#
# try:
#     num = 1/0
#     print(num)
# except Exception:
#     err_msg = traceback.format_exc()
#     print(err_msg)
#
import traceback

# try:
#     num = 1/0
# except Exception:
#     err_msg1 = traceback.format_exc()
#     print(err_msg1)
# else:
#     print("NO error")
# finally:
#     print("finally")


# def int_(str):
#     try:
#         result = int(str)
#         return result
#     except:
#         print("no")
#         return result
#     else:
#         return result+10
#     finally:
#         result = 100
#         return result
#
# num =int_('10')
# print(num)