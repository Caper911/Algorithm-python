#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 22:52:47 2017

@author: caper911
"""

def Merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #将剩余的元素复制到排好序的数组中
    result += left[i:]
    result += right[j:]
    return result
 
def MergeSort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)
  
if __name__=='__main__':  
    seq = [3,4,1,2,9,8]

    print('######Shell Sort')
    print('##Before Sort:\n',seq)

    print('##After Sort:')
    seq1 = MergeSort(seq)
    print(seq1)