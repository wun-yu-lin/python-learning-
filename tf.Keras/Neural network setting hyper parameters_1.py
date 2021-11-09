# -*- coding: utf-8 -*-

"""
Created on Tue Nov  9 17:23:32 2021

@author: wunyu
"""

#hyper parameters
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

#建立資料與前處理 
(x_train,y_train),(x_test,y_test) = mnist.load_data()
x_train = x_train.reshape(x_train.shape[0],784)
x_test = x_test.reshape(x_test.shape[0],784)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#建立神經網路
model=Sequential()

#hyper parameter1: hidden layer
model.add(Dense(256,activation="sigmoid",input_dim=x_train.shape[1]))
model.add(Dense(128,activation="relu"))

#hyper parameter2: add dropout layer
model.add(Dropout(rate=0.5))
model.add(Dense(10, activation="softmax"))

#hyper parameter3: loss function and optimizers
sgd = optimizers.SGD(learning_rate=0.01)
model.compile(optimizer=sgd,loss="binary_crossentropy",metrics=["accuracy"])


#hyper parameter4: batch_size(訓練批次量)
#hyper parameter5: epochs(訓練週期)
history = model.fit(x_train, y_train, verbose=1, batch_size=32, epochs=50)

plt.figure(figsize=(5,5),dpi=300)
plt.plot(history.history["accuracy"],label="accurary")
plt.ylabel("accurary")
plt.xlabel("epoch")
plt.legend()
plt.show()

score = model.evaluate(x_test, y_test, verbose=1)
evaluate_loss =score[0]
evaluate_acc =score[1]
