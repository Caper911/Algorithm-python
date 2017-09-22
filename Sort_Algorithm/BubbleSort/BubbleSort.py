#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 22:17:23 2017

@author: caper911
"""

def bubbleSort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(0 , count-i-1):
            if lists[j] > lists[j+1]:
                lists[j], lists[j+1] = lists[j+1], lists[j]
    return lists


s = [3,4,1,2,9,8,5,6,7,10,11,7,0,0,1,2,3,4]

print('######Bubble Sort')
print('##Before Sort:\n',s)

print('##After Sort:')
s1 = bubbleSort(s)
print(s1)