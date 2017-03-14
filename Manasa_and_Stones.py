# get number of cases
n_case = int(input().strip())

for i_case in range(n_case):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    if (a == b):
        print(a * (n-1))
    else:
        if (a > b):
            large_step = a
            small_step = b
        else:
            large_step = b
            small_step = a
        values = []
        for i in range(n):
            value = large_step * i + small_step * (n-1-i)
            values.append(str(value))
        print(' '.join(values))