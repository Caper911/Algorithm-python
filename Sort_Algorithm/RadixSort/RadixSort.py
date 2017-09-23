#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:55:10 2017

@author: caper911
"""

import math
def RadixSort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    
    bucket = [[] for i in range(radix)]
    
    for i in range(1, k+1):
        for j in lists:
            bucket[j // (radix**(i-1)) % radix].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists


if __name__=='__main__':  
    seq = [710,342,45,686,6,841,428,134,68,264]

    print('######Radix Sort')
    print('##Before Sort:\n',seq)

    print('##After Sort:')
    seq1 = RadixSort(seq)
    print(seq1)