# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 11:02:44 2021

@author: wunyu
"""

# RandomForestClassifier隨機森林為使用多個decision tree的組合來建立模型
# n_estimators 可作為限制decision tree的數量，預設值為100
# RandomForestClassifier(n_estimators)

# 預設decision tree的組合為隨機的，若希望為固定方式將資料進行分配，可以使用 random_state 參數指定亂數種子
# RandomForestClassifier(random_state)

# RandomForestClassifier參數調整

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot as plt

dx,dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
plt.figure()
plt.scatter(dx_std.T[0],dx_std.T[1],c=dy,cmap="Dark2")
dx_train,dx_test,dy_train,dy_test = train_test_split(dx_std,dy,test_size=0.2,random_state=0)

score_training_save=[]
score_testing_save=[]
cv_score = []

#參數
cv=5
max_depth=3
n_est = [x*50 for x in range(1,10)]
n_est_str = [str(x) for x in n_est]

# training
for x in n_est:
    tree = RandomForestClassifier(n_estimators=x,max_depth=max_depth, random_state=0)
    tree.fit(dx_train,dy_train)
    score_training_save.append([tree.score(dx_train,dy_train)])
    score_testing_save.append([tree.score(dx_test,dy_test)])
    cv_score.append([cross_val_score(tree,dx_train,dy_train,cv=cv).mean()])
plt.figure(figsize=(10,10),dpi=300)
plt.plot(n_est_str,score_training_save,label="training data",color="b")
plt.plot(n_est_str,score_testing_save,label="testing data",color="r")
plt.plot(n_est_str,cv_score,label="N-fold val score",color="g")
plt.title("RandomForestClassifier()  n_estimators ")
plt.ylabel("accuracy")
plt.xlabel("n_estimators")
plt.legend()
plt.show()