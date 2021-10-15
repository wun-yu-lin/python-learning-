# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 23:18:18 2021

@author: wunyu
"""
#________________________________________________________
# str.split() 分割字串為list元素
list = 字串.split(分割字元,分割次數)

string1 = "Helle nico is a good band"
print(string1.split(" "))

string2 = "abcdabcdabcdabcdabcdabcdabcd"
string2.split("b",2)
Out: ['a', 'cda', 'cdabcdabcdabcdabcdabcd']

#使用 re module來分割string, 使用"多種"符號分割
import re
list 變數 = re.split("[分割符號]",字串)
string3 = "today is a good,day. Are you sure? I don't think so"
re.split("[,.]",string3)
Out: ['today is a good', "ay. Are you sure? I don't think so"]

#________________________________________________________

#使用 for loop 依序將元素處理
a = [1,2,-2,-3,3,4,-2]
new=[]
for x in a:
    new.append(abs(x))


#能逐次處理元素的map()函式  ##高階函式!!
map(函式function,容器containers)
a = [1,2,-2,-3,3,4,-2]
new = list(map(abs,a))

##_________________________________________________________
#使用filter() 篩選容器元素
#建立條件篩選容器中的元素
str_list = ['today is a good', 'day', " Are you sure? I don't think so"]
filed_str = list(filter(lambda x: len(x)>=5, str_list))

ST5 = lambda x : len(x)>=5  
filed_str = list(filter(ST5, str_list)) #lambda先建立判斷條件 再傳入filter做篩選

#__________________________________________________________

sorted(容器, key=函式, reverse=False)  #False 小到大 , True 大到小
string5 = ["aaa","bb","c","dddd","eeeeee"]
print(sorted(string5, key=len, reverse=True))
['eeeeee', 'dddd', 'aaa', 'bb', 'c']

#__________________________________________________________
#list 生成式
# 運算式 for 變數 in 容器]
#for loop 寫法
新容器 = []
for 變數 in 容器:
    新容器.append(運算式)
    
新容器=[abs(x) for 變數 in 容器]
#map寫法
新容器=list(map(abs,容器))

# [運算式 for 變數 in 容器 if 判斷式]
list111 = [1,2,3,4,5,6,7,8,9]
print([x for x in list111 if x > 4 ])

a =[1,2,3,4,5,6,7,8]
b =[2,3,4,5,6,7,8,9]
print([[x,y] for x,y in zip(a,b)])
print([x*y for x,y in zip(a,b)])

#list 生成式形成巢狀list
a = [1,2,3]
b = ["A","B"]
print([([x,y] for x in a) for y in b])  ###跑步出來很怪

















