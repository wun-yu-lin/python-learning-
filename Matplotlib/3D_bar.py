# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:12:54 2021

@author: wunyu
"""

#ax.bar3d(x軸起點,y軸起點,z軸起點,x軸高度,y軸高度,z軸高度)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig =plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection="3d")

np.random.seed(100)

#bar位置
x=np.arange(100)
y=np.arange(100)
z=np.zeros(100)


hx=np.ones(100)
hy=np.ones(100)
hz=np.arange(100)
ax.bar3d(x,y,z,hx,hy,hz)

plt.show()