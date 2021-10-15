# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 18:06:45 2021

@author: wunyu
"""

import numba as nb
import time

def add1(t):
    start = time.time()
    s=0
    for i in range(t):
        s+=i
    onlytime=time.time()-start
    return  onlytime



@nb.jit()
def add_with_jit(t):
    start = time.time()
    s = sum(range(1, t))
    onlytime = time.time() - start
    return onlytime

print("普通的for迴圈{}".format(add1(100000000)))
print("python內建函式+jit{}".format(add_with_jit(100000000)))