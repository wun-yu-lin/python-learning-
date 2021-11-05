# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 22:49:24 2021

@author: wunyu
"""

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
dx, dy = load_breast_cancer(return_X_y=True)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx,dy,test_size=0.5,random_state=0)

cv = 5
cv_scores = []
score_training_save=[]
score_testing_save=[]
z = [x for x in range(1,10)]
for x in z:
    knn = KNeighborsClassifier(n_neighbors=x)
    knn.fit(dx_train,dy_train)
    score_training_save.append([knn.score(dx_train,dy_train)])
    score_testing_save.append([knn.score(dx_test,dy_test)])
    cv_scores.append([cross_val_score(knn,dx_train,dy_train,cv=cv).mean()])
    
plt.figure(figsize=(10,10))
plt.plot(z,score_testing_save, label="testing data",color="r")
plt.plot(z,score_training_save, label="training data",color="b")
plt.plot(z,cv_scores,label="N-fold val score",color="g")
plt.legend()
plt.grid(True)
plt.show()