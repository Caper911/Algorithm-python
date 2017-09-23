### 希尔排序算法
**希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。**
****
#### 算法思想
**把待排序的数据元素分成若干个小组，对同一小组内的数据元素用直接插入法排序；<br>小组的个数逐次减少；<br>当完成了所有元素数据都在一个组内的排序后，排序过程结束。**

#### (存在原因)
**原始数据元素序列越接近有序，直接插入排序算法的时间效率就越高。<br>也就是因为这个的原因，才有了直接插入排序法的改进版:</br>希尔排序算法**

#### 复杂度
**若增量的取值合理的话，希尔排序算法的时间复杂度约为O(n(lbn)^2) 空间复杂度为O(1)<br>不是一种稳定的排序算法**
****
###代码实现
```
def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count / step
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
        group /= step
    return lists
```