# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 14:36:10 2021

@author: wunyu
"""

##特殊dict容器，collention模組中的特殊dict，稱為defaultdict(函式,dict)
from collections import defaultdict
dict=defaultdict(函式,dict)
lst = ["hello","nico","vast","hast","band"]
d = defaultdict(int)
for item in lst:
    d[item]+=1
print(d)

prices =[
    ['apple',50],
    ['banana',120],
    ['grape',500],
    ['apple',70],
    ['banana',150],
    ['banana',700]
    ]
fruits = defaultdict(list)



for name, price in prices:
    fruits[name].append(price)
for name, price in fruits.items():
    print(name,price)
    
