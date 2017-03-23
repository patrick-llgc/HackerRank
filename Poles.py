#!/bin/python3

import sys

"""
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]

for a0 in range(n):
    x_i,w_i = input().strip().split(' ')
    x_i,w_i = [int(x_i),int(w_i)]
"""
# 
n, k = 6, 2
xs = [10, 12, 16, 18, 30, 32]
ws = [15, 17, 18, 13, 10, 1]
costs = {}
costs[n] = 0
def find_cost(k):
    if k == n:
        return costs[n]
    for i in range(n-1, k-1, -1):
        print(i)
        cost = float('inf')
        idx = -1
        for j in range(1, len(xs)):
            if cost > ws[j] * (xs[j]-xs[j-1]):
                cost = ws[j] * (xs[j]-xs[j-1])
                idx = j
        # combine idx to idx-1
        ws[idx-1] += ws[idx]
        print('moving {} to {}'.format(idx, idx-1))
        del(ws[idx])
        del(xs[idx])
        costs[i] = costs[i+1] + cost
        print('xs:{}\nws:{}\n{}'.format(xs, ws, costs[i]))

    return costs[k]

print(find_cost(1))
