# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 03:14:44 2021

@author: wunyu
"""

# 藉由常規化(Regularization)來使model對於資料誤差的敏感度降低，適當的C可避免模型overfitting
# C 值會小，Regularization的效果就越強，減少離群值的影響，盡可能的加大決策邊界
# max_iter為最大迭代次數
# 如 console 出現 "ConvergenceWarning: Liblinear failed to converge" 代表迭代次數不足無法求出最佳解

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import LinearSVC 
from matplotlib import pyplot as plt

score_training_save=[]
score_testing_save=[]
cv_scores = []
cv=5
x = [10**i for i in range(-4,5) ]
x_str = [str(n) for n in x]

dx,dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)

plt.figure(figsize=(10,10))
plt.scatter(dx_std.T[0],dx_std.T[1],c=dy,cmap="Dark2")
plt.title("Scaled")
plt.grid()
plt.show()

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std,dy,test_size=0.2,random_state=0)

for c in x:
    lin_svc = LinearSVC(C=c,max_iter=10000000,verbose=True) #max_iter為最大迭代次數
    lin_svc.fit(dx_train,dy_train)
    cv_scores.append([cross_val_score(lin_svc,dx_train,dy_train,cv=cv).mean()])
    score_training_save.append([lin_svc.score(dx_train,dy_train)])
    score_testing_save.append([lin_svc.score(dx_test,dy_test)])
plt.figure(figsize=(10,10))
plt.plot(x_str,score_testing_save, label="testing data",color="r")
plt.plot(x_str,score_training_save, label="training data",color="b")
plt.plot(x_str,cv_scores,label="N-fold val score",color="g")
plt.xlabel("parameter c")
plt.ylabel("accurary")
plt.legend()
plt.grid(True)
plt.show()