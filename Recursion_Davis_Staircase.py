def count_ways_recursion(n):
    # without saving, very slow
    if n == 1 or n == 0:
        return 1
    n_ways = 0
    for num in [n-1, n-2, n-3]:
        if num >= 0:
            n_ways += count_ways(num)
    return n_ways

def count_ways(n):
    """A fancier Fibonacci series"""
    table = {1: 1, 0: 1, 2: 2}
    def count_ways(n):
        if n not in table:
            table[n] = count_ways(n-2) + count_ways(n-1) + count_ways(n-3)
        return table[n]
    return count_ways(n)

def count_ways_3caches(n):
    a = [1, 1, 2]
    for i in range(3, n+1):
        # always get the sum from the three numbers
        a[i%3] = a[0] + a[1] + a[2]
    return a[n%3]
    
s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(count_ways_3caches(n))
