#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]
alice_score = int(a0 > b0) + int(a1 > b1) + int(a2 > b2)
bob_score = int(a0 < b0) + int(a1 < b1) + int(a2 < b2)
print('{} {}'.format(alice_score, bob_score))
