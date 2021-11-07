# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 18:28:00 2021

@author: wunyu
"""

# RandomizedSearchCV 可以針對特定範圍的數值來進行參數測試，可以快速找到適當的參數
# GridSearchCV 是大範圍的搜尋最佳參數，當參數很多時容易有運算非常耗時的現象
# 如需運算細微的參數使用GridSearchCV會算到天荒地老



from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,GridSearchCV,RandomizedSearchCV
from sklearn.svm import SVC
import numpy as np
from matplotlib import pyplot as plt

dx,dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train,dx_test,dy_train,dy_test = train_test_split(dx_std,dy,test_size=0.2,random_state=0)

plt.figure(figsize=(10,10))
plt.scatter(dx_std.T[0],dx_std.T[1],c=dy,cmap="Dark2")
plt.title("load_breast_cancer")
plt.grid()
plt.show()

# =============================================================================
# #GridSearchCV #以下設定共有4000種組合，運算相當耗時
c = np.linspace(1,100,100) #100種
gmma =np.linspace(0.01,100,100) #100種
x_str = [str(i) for i in c]

para_grid ={"C":c,"gamma":gmma,"kernel":["linear","rbf","poly","sigmoid"]} #4種
model_grid = GridSearchCV(SVC(), param_grid=para_grid)
model_grid.fit(dx_train,dy_train)
Best_para_grid = model_grid.best_params_
CV_score_grid = model_grid.best_score_.round(3)
Test_score_grid = model_grid.score(dx_test,dy_test).round(3)
# =============================================================================


# =============================================================================
# #RandomizedSearchCV
# model = RandomizedSearchCV(estimator, para_grid, n_iter) #n_itern隨機搜尋參數組成的次數,預設為10次
# 使用n_iter=1000修改隨機搜尋得參數
c = np.linspace(1,100,100) #100種
gmma =np.linspace(0.01,100,100) #100種
x_str = [str(i) for i in c]
para_Rand ={"C":c,"gamma":gmma,"kernel":["linear","rbf","poly","sigmoid"]} #4種
model_Rand = RandomizedSearchCV(SVC(), param_distributions=para_Rand, n_iter=1000) #隨機搜尋的參數組合次數1000次
model_Rand.fit(dx_train,dy_train)
Best_para_Rand = model_Rand.best_params_
CV_score_Rand = model_Rand.best_score_.round(3)
Test_score_Rand = model_Rand.score(dx_test,dy_test).round(3)
# =============================================================================











