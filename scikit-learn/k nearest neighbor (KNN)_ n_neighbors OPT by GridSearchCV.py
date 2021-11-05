# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 23:43:15 2021

@author: wunyu
"""

# 除了人工搜尋K值的預測參數外，亦可使用網格搜尋(grid search)
# 調教後的模型 = GridSearchCV(estimator,param_grid) #param_grid為dict型態方式傳入
# param_grid = {"參數名稱":範圍,"參數名稱":範圍,.....}


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import GridSearchCV

dx, dy = load_breast_cancer(return_X_y=True)
dx_train, dx_test, dy_train, dy_test = train_test_split(dx,dy,test_size=0.5,random_state=0)

param_grid = {"n_neighbors":np.arange(1,11)}

model = GridSearchCV(KNeighborsClassifier(),param_grid=param_grid)

model.fit(dx_train,dy_train)

print("Best para:",model.best_params_)
print("CV score:",model.best_score_.round(3))
print("test score:",model.score(dx_test,dy_test).round(3))