#!/bin/python3

import sys

class Solution(object):
    def encryption(self, s):
        """Print string in a row-major semi-square and print out by column"""
        L = len(s)
        m = int(L ** 0.5)
        if L == m ** 2:
            n = m
        else:
            # n_col is n, n_row is m
            n = m + 1
            if m * n < L:
                m = m + 1
        word_list = []
        for i in range(n):
            word_list.append(s[i:L:n])
        return(' '.join(word_list))

if __name__ == "__main__":
    s = input().strip()
    print(Solution().encryption(s))
    
