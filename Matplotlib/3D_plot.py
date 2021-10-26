# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:21:09 2021

@author: wunyu
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(-2*np.pi,2*np.pi)
x,y = np.meshgrid(t,t) #建立平面網格
z = np.sin(np.sqrt(x**2+y**2))
z =x*y



fig =plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1,projection="3d")  #建立3D畫布
ax.plot_surface(x,y,z,cmap='viridis')  #劃出三軸建立的曲面x,y,z都必須是2D array

plt.tight_layout()
plt.show()