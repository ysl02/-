def merge_sort(alist):
    n = len(alist)
    #结束递归的条件
    if n <= 1:
        return alist
    #中间索引
    mid = n//2

    left_li = merge_sort(alist[:mid])
    print(left_li)
    right_li = merge_sort(alist[mid:])
    print(right_li)

    #指向左右表中第一个元素的指针
    left_pointer,right_pointer = 0,0
    #合并数据对应的列表：该表中存储的为排序后的数据
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        #比较最小集合中的元素，将最小元素添加到result列表中
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    #当左右表的某一个表的指针偏移到末尾的时候，比较大小结束，将另一张表中的数据（有序）添加到result中
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result

alist = [3,8,5,7,6]
print(merge_sort(alist))