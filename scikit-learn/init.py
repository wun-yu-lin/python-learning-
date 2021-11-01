# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 14:21:25 2021

@author: wunyu
"""

# =============================================================================
# ML主要是透過training dataset and testing dataset，來進行訓找出數據中潛藏的pattern
# 藉此建立模型，並且對新資料進行預測
# ML 可分為監督式學習 (Supervised learning) 及非監督式學習 (unsupervised learning)
# 分類方法可以分為 二元分類 (binary classification) 及 多元分類 (multi-class classification)  #scikit-learn預設是使用多元分類法
# =============================================================================


# =============================================================================
# Workflow of classification
# 1.Data collection (collect and label)
# 2.Data pre-processing (clean, integration and transport)
# 3.Model selection (choose Classifier)
# 4.Model training (setup hyperparameter設定超參數來訓練模型)
# 5.Model prediction (testing accurary and fitting of training model)
# =============================================================================


# =============================================================================
# #data preparation
# 
# #亂數建立dataset
# #make_blobs(n_samples,n_features,centers,random_state)

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

dx,dy = make_blobs(n_samples=10000,n_features=2,centers=2,random_state=0)
plt.figure(figsize=(10,10))
plt.scatter(dx.T[0],dx.T[1],c=dy,cmap="cool")
plt.title("No Scaled")
plt.grid(True)
plt.show()
# =============================================================================

# =============================================================================
# ##data standardization 加速模型訓練速度
# 
# #StandardScaler().fit_transform(data) #平均數=0,1變異數=1
# #MinMaxScaler().fit_transform(data) #資料在0-1之間
# #RobustScaler().fit_transform(data) #Q1-Q3外的點會大於1 其餘會0-1之間
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
dx,dy = make_blobs(n_samples=10000,n_features=10,centers=2,random_state=0)
dx_std = StandardScaler().fit_transform(dx)
plt.figure(figsize=(10,10))
plt.scatter(dx_std.T[0],dx_std.T[1],c=dy,cmap="Dark2")
plt.title("Scaled")
plt.grid()
plt.show()
# =============================================================================

#分割 training data and testing data
#train_test_split(data,label,test_size,random_state)
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
dx,dy = make_blobs(n_samples=500,n_features=2,centers=2,random_state=0)
dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test= train_test_split(dx_std,dy,test_size=0.2,random_state=0) #20%當testing data 剩餘80%當training data


