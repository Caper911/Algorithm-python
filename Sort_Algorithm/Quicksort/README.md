## 快速排序算法
**快速排序算法是一种基于二叉树结构的交换排序方法(挖矿填坑+分治法)**
<br>
***
#### 基本思想
**设序列中有n个元素[a1,a2,a3,...,an]，<br>以第一个数据a1为基准数(把a1数挖出来形成一个坑)，<br>首先从右往左扫描，寻找比a1小的数(假设是a3)，<br>再把a3挖出来填到之前a1形成的坑那里，然后再从左往右扫描，寻找比基准数a1大的数填到a3形成的坑。<br>终止条件是左侧的数都比基准数小，右侧的数都比基准数大(或者说寻找指针i=j,把基准数回填到a[i])。**
***
#### 实现代码如下(Python)
 
```
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
```