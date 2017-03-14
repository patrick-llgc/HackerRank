#!/bin/python3

import sys

class Solution(object):
    def count_evenly_divisible_digits(self):
        """ Find how many digits can evenly divide the integer. """
        t = int(input().strip())
        for a0 in range(t):
            n = int(input().strip())
            # since there are only 10 possible results
            # record previously known results
            digit_dict = {}
            counter = 0
            for t_char in str(n):
                t_char = int(t_char)
                if t_char == 0:
                    continue
                if t_char in digit_dict.keys():
                    counter = counter + digit_dict[t_char]
                elif (n % t_char == 0):
                    digit_dict[t_char] = 1
                    counter = counter + 1
                else:
                    digit_dict[t_char] = 0
            print(counter)

if __name__ == "__main__":
    Solution().count_evenly_divisible_digits()
