# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 00:20:39 2021

@author: wunyu
"""

#建立切分list之function
def slice_list(ls,n_part):
    if not isinstance(ls,list) or not isinstance(n_part,int):
        return []
    ls_len = len(ls)
    if n_part<=0 or 0==ls_len:
        return[]
    elif n_part ==ls_len:
        return [[x] for x in ls]
    else:
        j = ls_len//n_part
        ls_return = []
        #利用迴圈將List分part傳入list 形成蜂槽式list
        for i in range(0,(n_part-1)*j,j):
            print(i)
            ls_return.append(ls[i:(i+j)])
        #補上尾數list
        ls_return.append(ls[i+j:])
        return ls_return

#計算蜂槽式迴圈中，各list的元素數目
def len_list(ls_sliced):
    if not isinstance(ls_sliced,list):
        return
    else:
        ls_sliced_len = []
        
        for x in ls_sliced:
            k = len(x)
            ls_sliced_len+=[k]
        return ls_sliced_len