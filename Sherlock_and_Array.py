def arraySherlock(a):   
    """Return 1 if we can find a number where the sum on both ends equal"""
    left = 0
    right = len(a) - 1
    left_sum = a[left]
    right_sum = a[right]
    while (left != right):
        if left_sum > right_sum:
            right -= 1
            right_sum += a[right]
        else:
            left +=1
            left_sum += a[left]
    return left_sum == right_sum
     
if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = [int(num) for num in input().strip().split()]
        if arraySherlock(a):
            print ("YES")
        else:
            print ("NO")