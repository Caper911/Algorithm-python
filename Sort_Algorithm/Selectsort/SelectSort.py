#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 23:23:48 2017

@author: caper911
"""

def SelectSort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


s = [3,4,1,2,9,8,5,6,7,10,11,7,0,0,1,2,3,4]

print('######Select Sort')
print('##Before Sort:\n',s)

print('##After Sort:')
s1 = SelectSort(s)
print(s1)