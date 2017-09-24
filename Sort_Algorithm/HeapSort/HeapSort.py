#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:05:22 2017

@author: caper911
"""

## 构造最大堆
def BuildHeap(lists, size):
    for i in range(0, (size // 2))[::-1]:
        AdjustHeap(lists, i, size)


def AdjustHeap(lists, i, size):
    
    #i结点的左右子结点下标分别为[2i+1]和[2i+2]
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max_ = i
    if i < size // 2:
        if lchild < size and lists[lchild] > lists[max_]:
            max_ = lchild
        if rchild < size and lists[rchild] > lists[max_]:
            max_ = rchild
        if max_ != i:
            lists[max_], lists[i] = lists[i], lists[max_]
            AdjustHeap(lists, max_, size)
 

def HeapSort(lists):
    size = len(lists)
    BuildHeap(lists, size)
    # 把调整后的最大堆顶点放到序列后方
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        
        # 重新调整根节点使之满足最大堆
        AdjustHeap(lists, 0, i)
        
    return lists
if __name__=='__main__':  
    seq = [710,342,45,686,6,841,428,134,68,264]

    print('######Heap Sort')
    print('##Before Sort:\n',seq)

    print('##After Sort:')
    seq1 = HeapSort(seq)
    print(seq1)