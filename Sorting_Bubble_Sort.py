n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

n_swaps = 0
for i, _ in enumerate(a):
    t_swaps = 0
    for j, _ in enumerate(a[:-1]):
        if a[j+1] < a[j]:
            a[j+1], a[j] = a[j], a[j+1]
            t_swaps += 1
            n_swaps += 1
    if t_swaps == 0:
        break

print('Array is sorted in {} swaps.'.format(n_swaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[-1]))