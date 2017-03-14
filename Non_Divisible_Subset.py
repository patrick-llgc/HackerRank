#!/bin/python3

import sys

n, k = input().strip().split(' ')
n, k = [int(n),int(k)]

numbers = map(int, input().strip().split(' '))
# equivalent to 
# numbers = [int(number) for number in input().strip().split(' ')]

# initialize a residual dict / or list
residual_dict = {}
for i in range(k):
    residual_dict[i] = []
# build dict with keys being the values' residual mod k
for number in numbers:
    residual_dict[number % k].append(number)
max_set = 0
for i in range(1, (k + 1) // 2):
    max_set = max_set + max(len(residual_dict[i]), len(residual_dict[k-i]))
if k % 2 ==0 and residual_dict[k//2]:
    max_set = max_set + 1
if residual_dict[0]:
    max_set = max_set + 1
print(max_set)