#!/bin/python3

import sys

def make_change(coins, n):
    n_ways = [0] * (n+1)
    n_ways[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            n_ways[i] += n_ways[i-coin]
    return n_ways[n]
    

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
