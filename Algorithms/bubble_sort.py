# coding:utf-8

# 冒泡排序


def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        # print(i)
        for j in range(i):
            # print(j)
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


li = [54, 36, 93, 17, 77, 31, 44, 55, 20]

bubble_sort(li)
print(li)

