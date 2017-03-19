def isPrime(n):
    """Check prime with O(sqrt(N))"""
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        # make sure to check perfect square
        if n % i == 0:
            return False
    return True



p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
    

