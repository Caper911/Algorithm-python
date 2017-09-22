#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:57:36 2017

@author: caper911
"""

def quicksort(v, left, right):
    if left >= right:
        return v
    
    key = v[left]                       ##基准数key
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key):
            high -= 1
        v[low] = v[high]
        while (low < high) and (v[low] <= key):
            low += 1
        v[high] = v[low]
        
    v[low] = key
    if left < low:
        quicksort(v,left,low-1)
    if low < right:
        quicksort(v,high+1,right)
    
    return v

##测试数据
s = [6, 8, 10, 30, 6, 4, 11, 2, 2, 15, 6, 11, 3, 4, 5, 99,0]
#s=[]
print("######## Quick Sort")
print("#Before sort:\n",s)
s1 = quicksort(s, left = 0, right = len(s) - 1)
print("#After sort:\n",s1)