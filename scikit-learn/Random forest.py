# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 12:56:36 2021

@author: wunyu
"""
# Random forest 隨機森林
# 由一群Decision tree來決策預測資料標籤，由一群decision tree進行決策的方式可以避免單獨決策樹容易overfitting的問題
# 由於資料是隨機分配給各decision tree，因此稱為Random forest

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

score_training_save=[]
score_testing_save=[]
score_diff=[]
#觀察training data與testing data比例的變化是否會使準確度改變，過少的traing data 是否會有overfitting的現象
for x in range(1,100):
    x=(1-x*0.01)
    

    #建立資料集，鳶尾花iris
    
    dx, dy = load_iris(return_X_y=True)
    dx_train, dx_test, dy_train, dy_test = train_test_split(dx,dy,test_size=x,random_state=0)
    
    #建立模型
    Random_tree = RandomForestClassifier()
    Random_tree.fit(dx_train,dy_train)
    predictions = Random_tree.predict(dx_test)
    score_training = Random_tree.score(dx_train,dy_train)  # 模型對於training data的準確度
    score_testing = Random_tree.score(dx_test,dy_test)  # 模型對於testing data的準確度
    # =============================================================================
    # 存取各參數結果
    score_training_save.append([score_training*100])
    score_testing_save.append([score_testing*100])
    score_diff.append([(score_training-score_testing)*100])
    # =============================================================================

#視覺化 cluster_std對於logistic regression之model運算的影響
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,1,1)
ax1.plot([x*0.01 for x in range(1,100)],(score_training_save),label="training data",color="b")
ax1.plot([x*0.01 for x in range(1,100)],(score_testing_save),label="testing data",color="r")
plt.title("RandomForest")
plt.grid(True)
plt.legend()
plt.ylabel("Accuracy")
plt.xlabel("training_size")

ax2 = fig.add_subplot(2,1,2)
ax2.plot([x*0.01 for x in range(1,100)],(score_diff),label="difference",color="black")
plt.grid(True)
plt.legend()
plt.xlabel("training_size")
plt.ylabel("difference of training and testing")
plt.show()
