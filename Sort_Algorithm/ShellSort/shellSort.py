#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 13:13:34 2017

@author: caper911
"""

def ShellSort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count // step

    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists

s = [3,4,1,2,9,8,5,6,7,10,11,7,0,0,1,2,3,4]

print('######Shell Sort')
print('##Before Sort:\n',s)

print('##After Sort:')
s1 = ShellSort(s)
print(s1)