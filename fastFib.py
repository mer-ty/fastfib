# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 17:36:51 2019

@author: acer
"""

def fastFib(num, memo = {}):
    if num == 0 or num == 1:
        return 1
    try:
        return memo[num]
    except KeyError:
        result = fastFib(num - 1, memo) + fastFib(num - 2, memo)
        memo[num] = result
        return result
for i in range(100):
    print(fastFib(i))
        
    