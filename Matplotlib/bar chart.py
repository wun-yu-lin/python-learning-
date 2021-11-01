# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 23:24:50 2021

@author: wunyu
"""

import numpy as np
import matplotlib.pyplot as plt

x = range(1,6)
y = np.random.choice(range(1,190),5)
y1 = np.random.choice(range(200,250),5)
y2 = np.random.choice(range(260,300),5)
plt.figure(figsize=(10,10))

labels = ["wunyu","winnie","emma","Royu","XD"]
#tick_label為標記x軸標籤
#堆疊bar圖bottom
plt.bar(x,y,tick_label=labels,label="y")
plt.bar(x,y1,tick_label=labels,bottom=y,label='y1')
plt.bar(x,y2,tick_label=labels,bottom=y1,label="y2")
plt.legend()
plt.show()
