### 基数排序
**基数排序也称为桶排序，是一种当数据类型为整数类型时非常高效的一种算法。**
****
#### 算法描述
**以整形数据为例(十进制数据有十个桶，八进制则有八个)，将所有元素按照个位数字分类，分类好后，将个位数字大小排列组合起来放到相应的桶中，然后按桶号从小到大和进入桶的先后次序收集分配在各桶的数据，然后就形成一个新的序列；<br>按再按照十位数字分类，再按照数字大小排列组合起来放到相应的桶中，再按上述收集方法形成新的序列,一直到最大数位为止。**

#### 复杂度
**时间复杂度为O(2mn) [n个数据 m次循环]**
****
#### 代码实现
```
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
```