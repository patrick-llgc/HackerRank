#!/bin/python3

import sys
from collections import Counter
def lonely_integer_counter(a):
    ct = Counter(a)
    keys = []
    for key in ct:
        if ct[key] == 1:
            keys.append(str(key))
    return ' '.join(keys)

def lonely_integer(a):
    result = 0
    for num in a:
        result ^= num
    return result

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
