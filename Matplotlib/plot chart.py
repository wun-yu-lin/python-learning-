# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 17:39:28 2021

@author: wunyu
"""

import matplotlib.pyplot as plt
import numpy as np



# #建立單張子圖,設定畫布大小
# plt.figure(figsize=(6,8))

# x = np.linspace(0,4*np.pi,num=100)
# y = np.sin(x)
# y1= np.cos(x)

# #plt.plot(x,y)  #資料
# plt.plot(x,y,color="g",label="sin(x)")   #plot可以畫折線圖
# plt.plot(x,y1,color="r",label="cos(x)")  #使用多格plot可畫多條

# plt.legend() #設定圖利，前面plt.plot需要加上label參數
# #plt.legend(["sin(x)","cos(x)"]) #也可使用list傳入legend設定圖例

# plt.xlim(0,13)  #定義X軸範圍
# plt.ylim(-1,1)   #定義y軸範圍

# plt.title("plot cahrt")  #title名稱

# plt.xlabel("x")  #x軸名稱
# plt.ylabel("y")  #y軸名稱

# plt.grid(True)  #是否使用網格 True or False

# x_ticks = []
# for z in range(5):
#     x_ticks=x_ticks+[z*np.pi]
# x_label = [0,90,180,270,360]
# plt.xticks(x_ticks,x_label)   #plt.xticks(ticks,label) #ticks代表刻度, label代表顯示的名稱

# #plt.show() #顯示plot出來
# plt.show()

##################################
#繪製多圖表，並切出子圖區
x = np.linspace(0,4*np.pi,num=100)
y = np.sin(x)
y1 = np.cos(x)
y2 = np.tan(x)
y3 = np.abs(x)
fig = plt.figure(figsize=(10,10),dpi=300) #建立畫布
# ax = fig.add_subplot(縱軸子圖數量n, 痕軸子圖數量m, 子圖編號n)
ax=fig.add_subplot(2,2,1)
ax.plot(x,y,color="g",label="sin(x)")

ax = fig.add_subplot(2,2,2)
ax.plot(x,y1,color="r",label="cos(x)")

ax= fig.add_subplot(2,2,3)
ax.plot(x,y2,color="g",label="tan(x)")

ax= fig.add_subplot(2,2,4)
ax.plot(x,y3,color="b",label="abs(x)") 
#fig.subplots_adjust(wspace=水平間,hspace=垂直間距)  #調整子圖間距
fig.subplots_adjust(wspace=0.2,hspace=0.2)

#技巧! 利用迴圈來畫多個子圖
for z in range(1,5):
    ax = fig.add_subplot(2,2,z)
    ax.set_xlim(0,13)
    #ax.set_ylim(0,13)
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.grid(True)
    if z == 1:
        ax.plot(x,y)
        ax.set_title("sin(x)")
    elif z ==2:
        ax.plot(x,y1)
        ax.set_title("cos(x)")
    elif z ==3:
        ax.plot(x,y2)
        ax.set_title("tan(x)")
    else:
        ax.plot(x,y3)
        ax.set_title("abs(x)")


fig.legend()
plt.show()


