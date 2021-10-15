# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 20:28:17 2021

@author: wunyu
"""

#機器學習領域進行資料 "預處理" 會使用的 lambda 來分割資料集
#或使用訓練資料和標籤時都會需要用到
#一般使用def定義函式
def func_name(參數):
    return 回傳值
#如果函式簡單，且只有一個回傳值的話，使用lambda 關鍵字
#lambda會將運算式自動變成回傳值，不需要寫return
func_name = lambda 參數:回傳值


#def 加 if 判斷式
def 絕對值(x):
    if x >= 0:
        return x
    else:
        return -x
#值a if 條件 else 值b  ##條件成立 回傳a ##條件不成立 回傳b
絕對值=lambda x: x if x>=0 else -x


def func(x):
    if 10<= x <30:
        return x**2-40*x+350
    else:
        return 50
    
func=lambda x: (x**2-40*x+350) if 10<= x <30 else 50