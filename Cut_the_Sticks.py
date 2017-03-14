#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while (arr):
    print(len(arr))
    cut_length = min(arr)
    arr = [stick - cut_length for stick in arr if stick - cut_length > 0]