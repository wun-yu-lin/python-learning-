# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 10:56:40 2021

@author: wunyu
"""

# 使用邏輯斯函數(logistic function)將特徵轉換成0-1之間的值，藉此來預測特定標籤或分類的機率
# logistic regression屬於二元分類器，藉由線性的分界或決策邊界 (decision boundary) 來區分資料
# 適合用於線性可分的數據!!
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression 
import matplotlib.pyplot as plt 

score_training_save=[]
score_testing_save=[]
score_diff=[]

#設定for loop進行反覆參數測試
for x in range(0,300):
    x=x*0.01
    
        
    # =============================================================================
    # #建立datasets dx=資料 dy=標籤
    
    dx,dy = make_blobs(n_samples=1000,n_features=2,centers=2,random_state=0,cluster_std=x)
    dx_std = StandardScaler().fit_transform(dx)
    # plt.figure(figsize=(10,10))
    # plt.scatter(dx_std.T[0],dx_std.T[1],c=dy,cmap="Dark2")
    # plt.title("Scaled, cluster_std=%f" %x)
    # plt.grid()
    # plt.show()
    dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std,dy,test_size=0.2,random_state=0)
    
    # =============================================================================
    # # 建立model
    # # 模型 = LogisticRegression()
   
    log_reg = LogisticRegression()
    log_reg.fit(dx_train,dy_train)
    prediction = log_reg.predict(dx_test)
    score_training = log_reg.score(dx_train,dy_train)  # 模型對於training data的準確度
    score_testing = log_reg.score(dx_test,dy_test)  # 模型對於testing data的準確度
    
    # =============================================================================
    # 存取各參數結果
    score_training_save.append([score_training*100])
    score_testing_save.append([score_testing*100])
    score_diff.append([(score_training-score_testing)*100])
    # =============================================================================
    
#視覺化 cluster_std對於logistic regression之model運算的影響
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,1,1)
ax1.plot([x*0.01 for x in range(0,300)],(score_training_save),label="training data",color="b")
ax1.plot([x*0.01 for x in range(0,300)],(score_testing_save),label="testing data",color="r")
plt.title("logistic regression")
plt.grid(True)
plt.legend()
plt.ylabel("Accuracy")
plt.xlabel("datasets cluster_std")

ax2 = fig.add_subplot(2,1,2)
ax2.plot([x*0.01 for x in range(0,300)],(score_diff),label="difference",color="black")
plt.grid(True)
plt.legend()
plt.xlabel("datasets cluster_std")
plt.ylabel("training-testing")

plt.show()