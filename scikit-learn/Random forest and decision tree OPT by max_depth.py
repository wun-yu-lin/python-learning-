# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 19:45:29 2021

@author: wunyu
"""

# DecisionTreeClassifier()及RandomForestClassifier()進行訓練的方式是產生決策數的節點 (node)，直到所有node的預測準確率都達到100%，或剩下樣品過少就停止
# 過度深層的node會導致model產生overfitting的問題，反而無法有效預測testing data
# 為了避免overfitting的問題，可以限制model分支的深度(層數)，使用max_depth參數來限制
# DecisionTreeClassifier(max_depth)
# RandomForestClassifier(max_depth)

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.tree import DecisionTreeClassifier,export_text
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

dx, dy = load_breast_cancer(return_X_y=True)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx,dy,test_size=0.2,random_state=0)



# =============================================================================
# #DecisionTreeClassifier() test max_depth
score_training_save=[]
score_testing_save=[]
cv_score = []
cv=5
max_depth_num = [x for x in range(1,15)]
max_str = [str(x) for x in max_depth_num]
for x in max_depth_num:
    tree = DecisionTreeClassifier(max_depth=x,random_state=0)
    tree.fit(dx_train,dy_train)
    score_training_save.append([tree.score(dx_train,dy_train)])
    score_testing_save.append([tree.score(dx_test, dy_test)])
    cv_score.append([cross_val_score(tree,dx_train,dy_train,cv=cv).mean()])
    
plt.figure(figsize=(10,10))
plt.plot(max_str,score_training_save,label="training data",color="b")
plt.plot(max_str,score_testing_save,label="testing data",color="r")
plt.plot(max_str,cv_score,label="N-fold val score",color="g")
plt.title("DecisionTreeClassifier() test max_depth")
plt.ylabel("accuracy")
plt.xlabel("max_depth")
plt.legend()
plt.show()
# =============================================================================
#畫出決策樹結構
feature_names = list(load_breast_cancer().feature_names)
export_re = export_text(tree, feature_names=feature_names)
export_re

# =============================================================================









# =============================================================================
# #RandomForestClassifier() test max_depth
score_training_save=[]
score_testing_save=[]
cv_score = []
cv=5
max_depth_num = [x for x in range(1,15)]
max_str = [str(x) for x in max_depth_num]
for x in max_depth_num:
    tree = RandomForestClassifier(max_depth=x)
    tree.fit(dx_train,dy_train)
    score_training_save.append([tree.score(dx_train,dy_train)])
    score_testing_save.append([tree.score(dx_test, dy_test)])
    cv_score.append([cross_val_score(tree,dx_train,dy_train,cv=cv).mean()])
    
plt.figure(figsize=(10,10))
plt.plot(max_str,score_training_save,label="training data",color="b")
plt.plot(max_str,score_testing_save,label="testing data",color="r")
plt.plot(max_str,cv_score,label="N-fold val score",color="g")
plt.title("RandomForestClassifier() test max_depth")
plt.ylabel("accuracy")
plt.xlabel("max_depth")
plt.legend()
plt.show()
# =============================================================================

