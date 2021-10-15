# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 12:09:07 2021

@author: wunyu
"""

#FunctionType 函式
#MethodType 方法


from types import MethodType,FunctionType
class Foo(object):
    
    
     def __init__(self):
         self.name="haiyan"
          
     def func(self):
         print(self.name)
         
obj = Foo()
print(isinstance(obj.func,FunctionType))  #False
print(isinstance(obj.func,MethodType))   #True   #說明這是一個方法
 
print(isinstance(Foo.func,FunctionType))  #True   #說明這是一個函式。
print(isinstance(Foo.func,MethodType))  #Falses




## 使用 @staticmethod靜態方法 或 @classmethod類方法 定義為 Function or method
class Foo(object):
    """類三種方法語法形式"""
 
    def instance_method(self):   #普通使用class的方法，需要使用引數，一般慣用self
        print("是類{}的例項方法，只能被例項物件呼叫".format(Foo))
 
    @staticmethod  ##可無視self 可作為一般Function使用
    def static_method():
        print("是靜態方法")
 
    @classmethod  ##引數必須為cls
    def class_method(cls):
        print("是類方法")