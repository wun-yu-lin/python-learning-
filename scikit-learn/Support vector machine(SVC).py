# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:15:52 2021

@author: wunyu
"""

# Support vector machine,SVM 支持向量機
# SVM 能夠將資料投射到更高維度的空間中，藉此讓數據可以分開並且找出超平面 (hyperplane)
# SVM 會進可能的拉大超平面兩側的決策邊界decision boundary
# 邊界的定義來自於hyperplane到某分類資料的最近距離，因此稱為支持向量
# SVM 運算比較耗效能訓練時間較長，分類效果通常比較好
# 這邊使用SVM 預設RBF(radial basis function 徑向基底函數)
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt

score_training_save=[]
score_testing_save=[]
score_diff=[]

for x in range(0,300):
    x=x*0.01

    # =============================================================================
    #建立blobs datasets dx=資料 dy=標籤
    dx,dy = make_blobs(n_samples=1000,n_features=2,centers=2,random_state=0,cluster_std=x)
    dx_std = StandardScaler().fit_transform(dx)
    # plt.figure(figsize=(10,10))
    # plt.scatter(dx_std.T[0],dx_std.T[1],c=dy,cmap="Dark2")
    # plt.title("Scaled cluster_std=%f"%x)
    # plt.grid()
    # plt.show()
    dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std,dy,test_size=0.2,random_state=0)
    # =============================================================================

    # =============================================================================
    #建立模型
    #模型 = SVC()
    SVC_m = SVC()
    SVC_m.fit(dx_train,dy_train)
    predictions = SVC_m.predict(dx_test)
    score_training = SVC_m.score(dx_train,dy_train)  # 模型對於training data的準確度
    score_testing = SVC_m.score(dx_test,dy_test)  # 模型對於testing data的準確度
    # =============================================================================
    # 存取各參數結果
    score_training_save.append([score_training*100])
    score_testing_save.append([score_testing*100])
    score_diff.append([(score_training-score_testing)*100])
    # =============================================================================

#視覺化 cluster_std對於linearSVC之model運算的影響
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,1,1)
ax1.plot([x*0.01 for x in range(0,300)],(score_training_save),label="training data",color="b")
ax1.plot([x*0.01 for x in range(0,300)],(score_testing_save),label="testing data",color="r")
plt.title("SVC")
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