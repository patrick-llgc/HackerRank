def count_inversions_simple(a):
    """This times out, O(n**2)"""
    n_reverse = 0
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                n_reverse += 1
    return n_reverse

def count_intra(a, start, end):
    if start >= end:
        return 0
    mid = (start + end) // 2
    count1 = count_intra(a, start, mid)
    count2 = count_intra(a, mid+1, end)
    count3 = count_inter(a, start, end)
    return count1+count2+count3

def count_inter(a, start, end):
    if start >= end:
        return 0
    mid = (start + end) // 2
    left = start
    right = mid + 1
    delta = 0
    counter = 0
    t_a = []
    while (left <= mid and right <=end):
        if a[left] > a[right]:
            delta = delta + 1
            t_a.append(a[right])
            right += 1
        else:
            counter += delta
            t_a.append(a[left])
            left += 1
    t_a.extend(a[left:mid+1])
    t_a.extend(a[right:end+1])
    a[start:end+1] = t_a
    counter += delta * (mid - left + 1)
    return counter

def count_inversions(a):
    return count_intra(a, 0, len(a)-1)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    print(count_inversions(arr))

        
