# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:36:06 2021

@author: wunyu
"""

# Decision tree 決策樹 為分類器的一種
# 訓練時以樹狀決策結構，結構由許多節點(node)組成，根據每個節點設定規則來分類資料，最終在每個節點(葉節點)得到資料標籤(class)
# 缺點是容易受到資料變動導致預測效果，容易有overfitting的問題

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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
    tree = DecisionTreeClassifier()
    tree.fit(dx_train,dy_train)
    predictions = tree.predict(dx_test)
    score_training = tree.score(dx_train,dy_train)  # 模型對於training data的準確度
    score_testing = tree.score(dx_test,dy_test)  # 模型對於testing data的準確度
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
plt.title("Decision tree")
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