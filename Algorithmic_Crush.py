# find the biggest accumulation point during a piecewise addition
# Hint: store the differences instead of actuall values
N, M = [int(num) for num in input().strip().split()]
diff = [0] * (N)
for i in range(M):
    i, j, k = [int(num) for num in input().strip().split()]
    diff[i-1] += k
    if j < N:
        diff[j] -= k
max_val = float('-Inf')
t_sum = 0
for num in diff:
    t_sum += num
    max_val = max(t_sum, max_val)
#print(dict_sum)
print(max_val)