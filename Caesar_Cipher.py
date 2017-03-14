#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())

new_s = ''
for char in s:
    pos = ord(char)
    if pos >= ord('a') and pos <= ord('z'):
        # it is a lower case
        new_pos = (pos - ord('a') + k) % 26 + ord('a')
        new_char = chr(new_pos)
    elif pos >= ord('A') and pos <= ord('Z'):
        # it is an upper case
        new_pos = (pos - ord('A') + k) % 26 + ord('A')        
        new_char = chr(new_pos)
    else:
        new_char = char
    new_s = new_s + new_char
print(new_s)