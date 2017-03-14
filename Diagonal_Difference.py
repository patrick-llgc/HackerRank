#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
sum_1 = 0
sum_2 = 0
for irow, row in enumerate(a):
    sum_1 = sum_1 + row[irow]
    sum_2 = sum_2 + row[n-1-irow]
difference = abs(sum_1 - sum_2)
print(difference)