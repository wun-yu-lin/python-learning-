# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:07:40 2021

@author: wunyu
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(10)
y = np.random.randn(10)
x1 = np.random.randn(10)
y1 = np.random.randn(10)
plt.figure(figsize=(10,10))

#散布圖 s=點大小 #cmap=整體色系

plt.scatter(x1, y1,color="b",label="Full scan",marker="o",s=100)
plt.scatter(x, y,color="r",label="DDA",marker="^",s=50)
plt.scatter(x, y,label="test",marker="^",s=50,cmap="rainbow")
plt.ylabel("m/z")
plt.xlabel("retention time")
plt.legend()
plt.show()

plt.figure(figsize=(10,10))
x = np.random.randn(100)
y = np.random.randn(100)
c = np.random.choice(range(20,50),100)
plt.scatter(x,y,s=c,c=c,cmap="Reds")