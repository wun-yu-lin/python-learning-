# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 23:05:03 2021

@author: wunyu
"""


import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10,10))
days =np.arange(1,101)
weights = np.random.choice(range(10,200),100)


plt.ylim([0,weights.max()+1])
plt.ylim([0,weights.max()+1])
plt.ylabel("weight")
plt.xlabel("days")

#設定資料點樣式及色彩
#plt.plot(x,y,marker=資料點樣式, markerfacecolor=顏色)
#設定線條樣式、寬度、顏色
#plt.plot(x,y,linestyle=線條樣式,linewidth=線條寬度)
plt.plot(days,weights,marker="o",markerfacecolor="b",label="random plot",linestyle="--",linewidth=0.5,color="g")





plt.legend()
plt.show()