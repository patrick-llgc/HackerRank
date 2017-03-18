#!/bin/python3

import sys

def heapify(a):
    """assume a[:-1] is in increasing order"""
    if len(a) < 2:
        return a
    val = a[-1]
    left = 0
    right = len(a) - 2
    while (left <= right): #
        mid = (left + right) // 2
        if a[mid] == val:
            left = mid
            break
        elif a[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    idx = left #
    a.insert(idx, val)
    a.pop()
    return a

def find_median(lowq, highq, a_t):
    if not lowq:
        lowq.append(a_t)
    elif len(lowq) <= len(highq):
        # insert into lowq
        if a_t <= highq[-1]:
            lowq.append(a_t)
            lowq = sorted(lowq)
        else:
            lowq.append(highq[-1])
            highq[-1] = a_t
            highq = sorted(highq, reverse=True)
    else:
        # insert into highq
        if a_t >= lowq[-1]:
            highq.append(a_t)
            highq = sorted(highq, reverse=True)
        else:
            highq.append(lowq[-1])
            lowq[-1] = a_t
            lowq = sorted(lowq)
  
    if (len(lowq) + len(highq)) % 2 == 0:
        median = (lowq[-1] + highq[-1])/2
    else:
        median = lowq[-1]
    return lowq, highq, median

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    n = len(a)
    a = heapify(a)
    if n % 2:
        median = a[int((n-1)/2)]
    else:
        median = (a[int(n/2 - 1)] + a[int(n/2)])/2.0
    print('{:.1f}'.format(median))


    