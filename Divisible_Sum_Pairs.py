#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
n_pair = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if ((a[i] + a[j]) % k == 0):
            n_pair += 1
print(n_pair)
        