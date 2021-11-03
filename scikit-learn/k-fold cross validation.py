# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 13:35:56 2021

@author: wunyu
"""

# k-fold cross-validation k-fold交叉驗證
# 除了trainging data and testing data 外，嚴謹的作法為還需要validation data來修正模型的參數，來確認模型的性能如何
# 將trainging data切成K等分，其中一等分當作validation data，依序將各等分當作validation data並算出accuracy的平均來評估模型

from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#進行k-fold cross-validation
#交叉驗證準確率 = cross_val_score(model,dx_train,dy_train, cv)  #cv為資料要切的等分,預設為5


# =============================================================================
#建立資料集，鳶尾花iris

dx, dy = load_iris(return_X_y=True)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx,dy,test_size=0.2,random_state=0)

#建立模型 & k-fold cross validation
Random_tree = RandomForestClassifier()
Random_tree.fit(dx_train,dy_train)
predictions = Random_tree.predict(dx_test)
Val_score = cross_val_score(Random_tree,dx_train,dy_train,cv=10)
score_training = Random_tree.score(dx_train,dy_train)  # 模型對於training data的準確度
score_testing = Random_tree.score(dx_test,dy_test)  # 模型對於testing data的準確度
# =============================================================================

#產生結果報告
#report = classification_report(dy_test,predictions)
report = classification_report(dy_test,predictions)
