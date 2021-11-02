# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:18:34 2021

@author: wunyu
"""
# K nearest neighbor (KNN) K最近鄰演算法
# Supervise learning 監督式分類器
# 不算train 因為是將原有數據進行新資料預判，所以learning運算量較小
# 良好的K值可使Model有適當的彈性
# K 值會大會導致 分類結果會趨向樣品數高的類別，所謂的underfitting
# K 值會小會導致 overfitting


from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier #KNN套件
import matplotlib.pyplot as plt 
# =============================================================================
# #建立datasets dx=資料 dy=標籤

dx,dy = make_blobs(n_samples=1000,n_features=2,centers=2,random_state=0,cluster_std=1)
dx_std = StandardScaler().fit_transform(dx)
plt.figure(figsize=(10,10))
plt.scatter(dx_std.T[0],dx_std.T[1],c=dy,cmap="Dark2")
plt.title("Scaled")
plt.grid()
plt.show()
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std,dy,test_size=0.2,random_state=0)
# =============================================================================


# =============================================================================
# # 建立KNN模型
# 模型 = KNeighborsClassifier(n_neighbor=k值) k值代表選用相近的幾個點進行預測

# 建立模型後，呼叫fit() method對traning data做訓練
# 模型.fit(dx_train,dy_train)  #input測試資料與標籤來進行訊練

# 接著對測試集的特徵資料做出預測
# 測試集特徵預測結果 = model.predict(dx_test)

# 檢視模型對training data and testing data的預測準確性(百分比)
# 模型.score(特徵資料, 標籤資料)
# knn = KNeighborsClassifier(n_neighbors=10)
# knn.fit(dx_train,dy_train)
# Predictions = knn.predict(dx_test)
# score_training = knn.score(dx_train,dy_train)  # 模型對於training data的準確度
# score_testing = knn.score(dx_test,dy_test)  # 模型對於testing data的準確度
# =============================================================================

score_training_save=[]
score_testing_save=[]
score_diff=[]
for x in range(1,101):
    knn = KNeighborsClassifier(n_neighbors=x)
    knn.fit(dx_train,dy_train)
    Predictions = knn.predict(dx_test)
    score_training = knn.score(dx_train,dy_train)  # 模型對於training data的準確度
    score_testing = knn.score(dx_test,dy_test)  # 模型對於testing data的準確度
    score_training_save.append([score_training*100])
    score_testing_save.append([score_testing*100])
    score_diff.append([(score_training-score_testing)*100])
    
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,1,1)
ax1.plot([x for x in range(1,101)],(score_training_save),label="training data",color="b")
ax1.plot([x for x in range(1,101)],(score_testing_save),label="testing data",color="r")
plt.title("K nearest neighbor (KNN)")
plt.grid(True)
plt.legend()
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")

ax2 = fig.add_subplot(2,1,2)
ax2.plot([x for x in range(1,101)],(score_diff),label="difference",color="black")
plt.grid(True)
plt.legend()
plt.xlabel("n_neighbors")
plt.ylabel("training-testing")

plt.show()









