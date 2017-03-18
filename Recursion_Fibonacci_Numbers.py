def fibonacci_recursion_wo_memory(n):
    # This times out
    if n==0 or n==1:
        return n
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_recursion_w_memory(n):
    def lookup(n, fibo):
        if n==0 or n==1:
            return n
        if n not in fibo:
            fibo[n] = lookup(n-1, fibo) + lookup(n-2, fibo)
        return fibo[n]
    return lookup(n, {})

def fibonacci_iteration(n):
    if n == 0 or n == 1:
        return n
    i = 2
    fibo = [0, 1]
    while i <= n:
        fibo[i%2] = fibo[0] + fibo[1]
        i += 1
    return fibo[n%2]

def fibonacci_dynamic(n):
    # Write your code here.
    fibo = {}
    fibo[0] = 0
    fibo[1] = 1
    if n==0 or n==1:
        return fibo[n]
    for i in range(2, n+1):
        fibo[i] = fibo[i-2] + fibo[i-1]
    return fibo[n]
        
n = int(input())
print(fibonacci_iteration(n))
