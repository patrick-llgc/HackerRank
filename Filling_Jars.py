import sys

N, M = input().strip().split(" ")
N, M = [int(N), int(M)]
sum = 0
for i in range(M):
    a, b, k = input().strip().split(" ")
    a, b, k = [int(a), int(b), int(k)]
    # we don't have to calculate and keep track of all numbers
    # since we are only interested in the total sum
    sum = sum + (b-a+1) * k


average = sum // N
print(average)
