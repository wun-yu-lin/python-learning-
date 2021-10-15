# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 13:51:06 2021

@author: wunyu
"""

import numpy as np
from numpy.random import rand
import time
N = 150 
matA = np.array(rand(N,N))
matB = np.array(rand(N,N))
matC = np.array([[0]*N for _ in range(N)])

#使用python計算_______________________________
start = time.time()
for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j]= matA[i][k]*matB[k][j]
            
print(float(time.time()-start))


#使用numpy計算________________________________
start= time.time()
matC =np.dot(matA,matB)
print(float(time.time()-start))

#____________________________________________
#np.array(lit/tuple...,dtype="None")
#np.arange(start,stop,step,dtype= "None")
print(np.arange(5))
print(np.arange(1,5))
print(np.arange(0,10,2))

#np.linspace(start,stop,num=50,dtype="None") 用於建立等差數列 指定元素數目作為參數
print(np.linspace(0,100,50))
#np.zeros / np.ones 建立全0或1的陣列
np.zeros(shape,dtype=float)
print(np.zeros(3))  #建立 0 axis 3元素
print(np.zeros([3,10])) #建立2 axis 3X10元素
print(np.zeros([3,10,3]))#建立3 axis 3X10X3元素

#np.random_____________________________________________________
np.random.seed(x)  #指定種子後，亂數會相同，不指定則反之。
x = np.random.randn(5)
print("x:",x)
np.random.seed(0)
x = np.random.randn(5)
print("x(seed=0):",x)
np.random.seed(1)
x = np.random.randn(5)
print("x(seed=1):",x)

#建立亂數array
#arr1
arr1 = np.random.randint(0,10,(10,10))  #0-10之間(不含10)隨機亂數建立10X10陣列
arr2 = np.random.rand(3,10) #建立0~1的亂數 3X10的陣列
#隨機取樣建立陣列
x = ["A","B","C","D","E","F"]
np.random.seed(0)
print(np.random.choice(x,10))  # x list中隨機取10元素

#container.copy() 使用copy來複製array 避免參照到相同記憶體位置

#______以下錯誤示範__________
arr1 =np.array([1,2,3,4,5])
print("arr1",arr1)
arr2 =arr1
arr2[0]=10
print("arr1",arr1)
print("arr2",arr2)

#_________使用copy()為正確方式___________
arr1 =np.array([1,2,3,4,5])
print("arr1",arr1)
arr2 = arr1.copy()
arr2[0]=10
print("arr1",arr1)
print("arr2",arr2)

#陣列切片
陣列物件[起始索引:終止索引:間格] = 變更的值
arr3 = np.arange(10)
print(arr3)
arr3[0:3]=1
print(arr3)

#布林陣列&篩選
new_arr = arr3<5
print(arr3[new_arr])

#陣列運算 + - * ** / 
storages = np.array([1,2,3,4])
storages+=storages
print(storages)
print(storages**2)
 
#數學運算式子
np.abs() # 絕對值
np.exp() # e 為底的值
np.sqrt() # 平方根
np.unique() #取消重複的元素
np.union1d() #聯集，去除重複元素，結合成新陣列
np.intersect1d #交集 取出共同有的元素
np.setdiff1d() #差集

#____________多軸陣列____________
arr = np.array([[1,2,3],[4,5,6]])
print(np.sum(arr)) #array所有元素加總
print(arr.sum())
print(arr.sum(axis=0)) #沿著 axis 0 進行加總
print(arr.sum(axis=1)) #沿著 axis 1 進行加總

#array 的 Shape
#陣列物件.shape
arr.shape

#重塑陣列的形狀(reshaping)
陣列物件名稱.reshaping(指定的shape)

#多軸array的切片作法
#idex
arr[0][0]
#切片slicing
arr[0,0:] 

#fancy indexing
arr1 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(arr1[[3,2,0]])

#轉置 transpose
陣列物件名稱.transpose(1,0) #原本(0,1) 改成 (1,0)
陣列物件名稱.T #無法指定參數 ex:(0,1,2) --> (2,1,0), (3,1,5) --> (5,1,3)
arr1.transpose(1,0)

#排序
np.sort(陣列物件,axis=-1)  #-1指得是最後一軸
陣列物件.sort(axis=-1)

#取得排序前的索引位置
np.argsort(陣列物件,axis=-1)  #-1指得是最後一軸
陣列物件.argsort(axis=-1)

#陣列擴張Broadcasting，當不同shape的陣列進行運算時，Shape較小的陣列會進行擴張，匹配較大的陣列
x=np.arange(15).reshape(3,5)
y=np.array([np.arange(5)])
z=x-y  #y的shape為(1,5)，當x-y時 y會自動擴張成(3,5)，每列都會重複
print(x)
print(y)
print(z)

#Array 內積
np.dot()

