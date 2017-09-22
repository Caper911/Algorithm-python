#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 00:05:06 2017

@author: caper911
"""

def insertSort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

s = [3,4,1,2,9,8,5,6,7,10,11,7,0,0,1,2,3,4]

print('######Select Sort')
print('##Before Sort:\n',s)

print('##After Sort:')
s1 = insertSort(s)
print(s1)