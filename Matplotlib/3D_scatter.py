# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:30:19 2021

@author: wunyu
"""

#ax.scatter3D(x,y,z)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(10,10))
ax=fig.add_subplot(1,1,1,projection="3d")



x = np.random.randn(1000)
y = np.random.randn(1000)
z = np.random.randn(1000)


#
ax.scatter3D(x,y,z,cmap="Blue")
plt.show()
