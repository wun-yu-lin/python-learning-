# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:14:23 2021

@author: wunyu
"""

# Deep learning 深度學習為利用多層的神經網路 (Neural Network) 從大量資料進行學習
# Neural Network 為多的ML model所組成，可以分成好幾層，每一層的Neural都會有input,weight,bias並經由計算後產生ouput y^，y^作為下一層model的input
# Neural Network 藉由資料來不斷修正weight,bias來提高預測的準確度越高越好

# 建立訓練模型的步驟
# 1. 建立神經網路模型 => 設計神經網路結構
# 2. 訓練神經網路模型 => training data and testing data 來訓練模型，並使用loss function來評估模型參數的好壞，經常使用back propagation的演算法來反覆調整weight,bias的參數
from tensorflow.keras.datasets import mnist #建立資料集模組
from tensorflow.keras.models import Sequential #序列式模型類別
from tensorflow.keras.layers import Dense #密集層類別
from tensorflow.keras.utils import plot_model #繪圖模組
from matplotlib import pyplot as plt #繪圖模組
from tensorflow.keras.utils import to_categorical #one-hot編碼
import numpy as np


# 進行數字照片的訓練
# 準備資料集
(x_train, y_train),(x_test,y_test) = mnist.load_data()
#print資料shape
print(x_train.shape,y_train,x_test.shape,y_test.shape)

# 數據前處理
x_train = x_train.reshape(x_train.shape[0],784) # 轉換數據形狀符合784個神經元的結構
x_test = x_test.reshape(x_test.shape[0],784)

y_train = to_categorical(y_train) #將標籤改為one-hot編碼
y_test = to_categorical(y_test)


#建立神經網路
model = Sequential() #建立神經網路，目前是空的
#使用add()來建立神經層, Dense=256為規劃256個neural, activation=sigmoid 指定model函數為sigmoid function
model.add(Dense(256,activation="sigmoid",input_dim=784))  # 加入第一層 (輸入層)
model.add(Dense(128,activation="relu")) #第二層(隱藏層), "relu" function 會將小於0的數值都轉成0
model.add(Dense(10,activation="softmax")) # 第三層(輸出層)

#參數編譯模型
model.compile(optimizer="rmsprop", #優化器
              loss="binary_crossentropy", #loss function
              metrics=["accuracy"]) #評量準則 
# 模型結構繪製
plot_model(model,show_shapes=True,show_layer_names=False)


# 訓練模型
#Verbose參數 => 訊息顯示模式 0=不顯示 1=完整(包含進度條), 2=精簡(不包含進度條)
#epoch參數 => 訓練週期 所有樣品訓練一次/周期
#batch_size參數 => 樣品分批給神經網路訓練的數目 (no. of sample/次)
history =model.fit(x_train,y_train,verbose=1,epochs=10,batch_size=32)
plt.figure(figsize=(5,5),dpi=300)
plt.plot(history.history["accuracy"],label="accurary")
plt.ylabel("accurary")
plt.xlabel("epoch")
plt.legend()
plt.show()

#評估模型成效
#使用evaluate()來評估成效
score = model.evaluate(x_test,y_test,verbose=1)
evaluate_loss =score[0]
evaluate_acc =score[1]


#用模型預測答案
plt.figure(figsize=(10,10),dpi=300)
for i in range(1,21):
    plt.subplot(1,20,i)
    plt.imshow(x_test[i-1].reshape((28,28)),"gray")
plt.show()

predictions = np.argmax(model.predict(x_test[0:20]),axis=1)
print(predictions)






















