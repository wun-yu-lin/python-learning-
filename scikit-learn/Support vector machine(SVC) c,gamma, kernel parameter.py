# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 14:19:57 2021

@author: wunyu
"""

# SVC() 擁有C參數來調整regularization的效果強度，也具有其他gamma, kernel參數可以使用
# SVC(C,gamma,kernel)

##gamma 參數: 單一資料點對於decision boundary的影響,越高代表每個資料點的影響力越弱，意思就是需要更多資料作為support vector
# gamma值越大，分界線與decision boundary會更貼近資料，型態比較扭曲, 預設為scale，可針對features數量調整參數

##Kernel 參數: poly,rbf,sigmoid,gamma
# Linear 線性函數: 用線性函數映射資料點，效果與linearSVC差不多
# poly 多項式函數: 採用多項式函數 (polynominal function) 來映射資料點
# rbf 徑向基底函數 (radial basis function) 來映射資料點，這也是SVC()預設值,分類效果通常比較好
# sigmoid sigmoid函數: 使用邏輯斯函數 (Logistic function) 來映射資料點，分類效果跟LogisticRegressiont差不多

#使用GridSearchCV()來搜尋SVC()之C,gamma, kernel最佳解，並視覺化


from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split,cross_val_score,GridSearchCV
from sklearn.svm import SVC
from matplotlib import pyplot as plt

dx,dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train,dx_test,dy_train,dy_test = train_test_split(dx_std,dy,test_size=0.2,random_state=0)

plt.figure(figsize=(10,10))
plt.scatter(dx_std.T[0],dx_std.T[1],c=dy,cmap="Dark2")
plt.title("load_breast_cancer")
plt.grid()
plt.show()
c=5
cv=5
x = [10**i for i in range(-4,3)]
x_str = [str(i) for i in x]
para_grid ={"C":x,"gamma":x,"kernel":["linear","rbf","poly","sigmoid"]}


model = GridSearchCV(SVC(), param_grid=para_grid)
model.fit(dx_train,dy_train)
Best_para = model.best_params_
CV_score = model.best_score_.round(3)
Test_score = model.score(dx_test,dy_test).round(3)


#Gamma值對於model的影響
score_training_save=[]
score_testing_save=[]
cv_scores = []
for z in x:
    SVC_model = SVC(C=c,gamma=z,kernel="rbf")
    SVC_model.fit(dx_train,dy_train)
    cv_scores.append([cross_val_score(SVC_model,dx_train,dy_train,cv=cv).mean()])
    score_training_save.append([SVC_model.score(dx_train,dy_train)])
    score_testing_save.append([SVC_model.score(dx_test,dy_test)])
    
plt.figure(figsize=(10,10),dpi=100)
plt.plot(x_str,score_testing_save, label="testing data",color="r")
plt.plot(x_str,score_training_save, label="training data",color="b")
plt.plot(x_str,cv_scores,label="N-fold val score",color="g")
plt.xlabel("gamma")
plt.ylabel("accurary")
plt.legend()
plt.grid(True)
plt.show()


#C值對於model的影響
score_training_save=[]
score_testing_save=[]
cv_scores = []
for z in x:
    SVC_model = SVC(C=z,gamma="scale",kernel="rbf")
    SVC_model.fit(dx_train,dy_train)
    cv_scores.append([cross_val_score(SVC_model,dx_train,dy_train,cv=cv).mean()])
    score_training_save.append([SVC_model.score(dx_train,dy_train)])
    score_testing_save.append([SVC_model.score(dx_test,dy_test)])
    
plt.figure(figsize=(10,10),dpi=100)
plt.plot(x_str,score_testing_save, label="testing data",color="r")
plt.plot(x_str,score_training_save, label="training data",color="b")
plt.plot(x_str,cv_scores,label="N-fold val score",color="g")
plt.xlabel("C")
plt.ylabel("accurary")
plt.legend()
plt.grid(True)
plt.show()