# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 21:36:35 2021

@author: wunyu
"""
## counter 快速統計 字詞出現"次數"
from collections import Counter
容器 = Counter(其他容器)

lst =["foo","bar","pop","foo","bar","foo"]
c = Counter(lst)

for item, counter in c.items():
    print(item,"出現",counter,"次")
print("出現最多次數的項目:",c.most_common(1))