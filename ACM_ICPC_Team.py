#!/bin/python3

import sys

def count_common (input_1, input_2, m):
    """
    Input: two strings, input_1 and input_2 (each char is either 1 or 0), m is the length
    Output: int, maximum number of nonzero digit when inputs are union'ed
    """
    if 1:
        common = 0
        for i in range(m):
            if (input_1[i] != '0' or input_2[i] != '0'):
                common = common + 1
    else:
        # alternative, slower and problematic method. 
        # if m is really large, int() may fail
        res = int(input_1) + int(input_2)
        digits = [int(digit) > 0 for digit in str(res)]
        common = sum(digits)
    return common
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = str(input().strip())
   topic.append(topic_t)

commons = []
max_common = 0
max_count = 0
for i1, input_1 in enumerate(topic):
    for i2, input_2 in enumerate(topic):
        if i1 > i2:
            common = count_common(input_1, input_2, m)
            if common > max_common:
                max_common = common
                max_count = 1
            elif common == max_common:
                max_count = max_count + 1
#            commons.append(count_common(input_1, input_2))

print(max_common)
print(max_count)