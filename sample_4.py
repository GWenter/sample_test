#!/D:/path/ python
# -*- coding: UTF-8 -*-
#
# @Project : sample_test
# @File    : sample_4.py
# @Date    :2022/1/11 : 10:12


# list

list_1 = ["a", "b", "c", "d"]

for n in list_1:
    print(n)

# name[开始索引：结束索引：步进]
# 前包含，后不包含

print(list_1[1:3])

# list[-1]最后一个
print(list_1[-1])


#  list[:-1]倒叙
print(list_1[::-1])

name = ["zs", "ls", "lk"]
print(name)

# 插入append，只能插到最后
name.append("gwt")
print(name)

# insert(n,name) 插入到下标为n的位置
name.insert(1, 'nick')
print(name)

list_2 = ['a', 'b', 'c', 'a']

# count(a) 计数a的个数
print(list_2.count("b"))

# del 删除
del list_2[0]
print(list_2)

# pop默认删除最后一个并返回删除元素
name = ['ab', 'ac', 'bc', 'cd']
print(name)
name.pop()
print(name)
print(name.pop(1))
print(name)

# remove(str) 删除对应元素str
movie = ['qw', 'we', 'er']
print(movie)
movie.remove('we')
print(movie)
#  list 嵌套for
list_3 = [[x, y] for x in range(1, 10) for y in range(1, x+1)]
print(list_3)



# tuple元组,有序，可重复，无法修改
tup1 = tuple('abc')
# tup1[1] = 'd' 报错，元组不可修改
print(tup1)
print(tup1[1])

# tuple中元组元素是可修改类型如列表时，可以修改列表元素值，但元组元素依旧无法修改
tup2 = (['zs', 22, 'lk'],['ls', 33, 'wu'])
# tup2[0]=['zs', 23,'ll'] 不可修改
tup2[0][1] = 33
print(tup2[0])  # 列表元素修改

# del tup2         删除整个元组
# print(tup2)       元组不存在

tup3 = ("zd", 23)
tup4 = ('zs', 33)
tup5 = tup3 + tup4  #叠加
print(tup5)

tup6 = tup3 * 2  #
print(tup6)


# 生成器 防止内存爆满
gen = (i for i in range(1,10))
print(gen)
print(gen.__next__())
print(gen.__next__())

