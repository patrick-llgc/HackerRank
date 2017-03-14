#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    n_choco = n // c
    # suppose we can always borrow one wrap from our imaginary and resourceful friend
    # and return the wrap to him after we bought and ate the chocolate, the essentail 
    # cost of wrap for choco is m-1 wraps for 1 choco. 
    n_wrap_for_choco = n_choco // (m-1)
    if n_choco % (m-1) == 0:
        # if we happen to run out of wraps after trading them all in
        # we shouldn't have been able to buy the last one
        n_choco = n_choco + n_wrap_for_choco -1
    else:
        n_choco = n_choco + n_wrap_for_choco
    print(n_choco)
