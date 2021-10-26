# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:09:18 2021

@author: wunyu
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.choice(range(0,100),5)

plt.figure(figsize=(10,10),dpi=300)
labels = ['A','B','C','D','E']
explode=[0,0,0.2,0,0]

#繪製圓餅圖 
#label標籤  
#autopct="%.3f%%"參數顯示百分比後三位
#explode=區塊向外推移的幅度
#shadow加入陰影
plt.pie(data,
        labels=labels,
        autopct="%.3f%%",
        explode=explode,
        shadow=True
        )
plt.tight_layout()
plt.show()