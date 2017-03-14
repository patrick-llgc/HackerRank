#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    n_present = 0
    for arr_time in a:
        if arr_time <= 0:
            n_present = n_present + 1
    if n_present < k:
        print('YES')
    else:
        print('NO')
