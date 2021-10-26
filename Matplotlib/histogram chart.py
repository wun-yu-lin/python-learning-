# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 23:38:26 2021

@author: wunyu
"""

import matplotlib.pyplot as plt
import numpy as np

dis_data = np.random.randn(1000000)


ax = plt.figure(figsize=(20,10))

#繪製直方圖 
#plt.hist(data,bins)   #bins設定橫軸的間距數量
#density=True 代表y軸改成出線機率
ax1= ax.add_subplot(1,2,1)
ax1.hist(dis_data,bins="auto", density=True,label='non-cumulative', color='r')
ax2= ax.add_subplot(1,2,2)
ax2.hist(dis_data,bins="auto", density=True,cumulative=True,label="cumulative",color="g")
ax.legend()
ax.show()