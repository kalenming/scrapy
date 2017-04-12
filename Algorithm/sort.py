# -*- coding: utf-8 -*-
import random
import time

def make_list(n):
    a = list()
    i = 0
    while i < n:
        a.append(random.randint(0,10000))
        i = i + 1
    return a


def bubble(a):
    start = time.clock()
    l = len(a) - 2
    i = 0
    while i < l:
        j = l
        while j >= i:
            if a[j+1] < a[j]:
                a[j],a[j+1] = a[j+1],a[j]
            j = j -1
        i = i +1
    end = time.clock()
    #print (a)
    print ('冒泡查询用时：%s' % (end-start))


def insert(a):
    # 插入排序
    start = time.clock()
    for i in range(1,len(a)):
        j = i -1
        temp = a[i]
        while j >= 0 and (temp < a[j]):
            a[j+1] = a[j]
            j = j -1
        temp = a[j]
    end = time.clock()
    print ('插入排序查询用时：%s' % (end - start))

#选择排序

def select(a):
    start = time.clock()
    for i in range(0,len(a)-1):
        min = a[i]
        for j in range(i+1,len(a)):
            if a[j] < min:
                min,a[j] = a[j],min
    # for i in range(0,len(a)):
    #     min = a[i]
    #     for j in range(i+1,len(a)):
    #         if a[j] < min:
    #             min,a[j] = a[j],min
    # #print (a)
    end = time.clock()
    print ('选择排序查询用时：%s' % (end - start))

def shell(a):
    start = time.clock()
    step = 2
    group = len(a) / step
    while group > 0:
        for i in range(0,group):
            j = i + group
            while j < len(a):
                k = j - group
                key = a[j]
                while k >= 0:
                    if a[k] > key:
                        a[k+group] = a[k]
                        a[k] = key
                    k = k - group
                j = j + group
        group = group / step
    print (a)
    end = time.clock()
    print ('希尔排序查询用时：%s' % (end - start))





if __name__ == "__main__":
    a = make_list(200)
    bubble(a)
    a = make_list(200)
    insert(a)
    a = make_list(200)
    select(a)
    a = make_list(200)
    shell(a)

