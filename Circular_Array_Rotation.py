#!/bin/python3

import sys


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
k = k % n
for a0 in range(q):
    m = int(input().strip())
    # after k rotation, the array becomes
    # a_{n-k}, ..., a_{n-1}, a_0, ..., a_{n-k-1}
    # we just need to tell if the requested index is within the first k elements or not
    if m < k:
        num = a[n-k+m]
    else:
        num = a[m-k]
    print(num)
    
