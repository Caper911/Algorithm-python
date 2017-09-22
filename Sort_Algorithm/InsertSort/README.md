### 直接插入排序
****
#### 基本思想
**顺序地把待排序的数据元素按其关键字的大小插入到已排序数据元素子序列中的适合位置。子序列的数据元素个数从只有一个数据元素开始，<br>逐次增大，当子集合大小最终和集合大小相同时，排序完毕。**

#### 复杂度
**期望时间复杂度为O(n^2) 空间复杂度为O(1)<br>直接插入排序是一种稳定的排序算法**


****
#### 代码实现
```
def insert_sort(lists):
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
```