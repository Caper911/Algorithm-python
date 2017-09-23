### 归并排序算法
**本算法是采用分治法（Divide and Conquer）的一个非常典型的应用**
***
#### 算法思想
**设序列中存放了n个数据元素，初始的时候把它们看成n个长度为1的有序子序列，然后从第一个有序子序列开始，把相邻的有序子序列两两合并。<br>得到[n//2]个长度为2的新的有序序列。<br>对这些新的有序子序列再进行合并排序。<br>如此重复，直到得到一个长度为n的有序序列；**

#### 代码思路
**归并排序的算法我们通常用递归实现，先把待排序区间[s,t]以中点二分，接着把左边子区间排序，再把右边子区间排序，最后把左区间和右区间用一次归并操作合并成有序的区间[s,t]**<br>
**比较左区间元素a[i]和右区间元素a[j]的大小，若a[i]≤a[j]，则将第一个有序表中的元素a[i]复制到result[k]中，并令i和k分别加上1；否则将第二个有序表中的元素a[j]复制到result[k]中，并令j和k分别加上1，如此循环下去，直到其中一个有序表取完，然后再将另一个有序表中剩余的元素复制到r中从下标k到下标t的单元。**

#### 复杂度
**时间复杂度为O(nlbn) 而且归并排序是一种稳定的排序算法，能保证原来在前边的数据排序后仍然在前边**

****
#### 代码实现
```
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
```