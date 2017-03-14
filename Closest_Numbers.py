#!/bin/python3
    
# parse the input
n = int(input().strip())
nums = [int(num) for num in input().strip().split(" ")]

# after sorting, just compare the neighrboing diffs
nums = sorted(nums)

# initialize
min_diff = float('inf') # note: sys.maxint is removed in python 3
for idx in range(1, len(nums)):
    diff = abs(nums[idx] - nums[idx-1])
    if diff < min_diff:
        min_pair = [sorted([nums[idx], nums[idx-1]])]
        min_diff = diff
    elif diff == min_diff:
        min_pair.append(sorted([nums[idx], nums[idx-1]]))

min_pair = sorted(min_pair, key=lambda x: x[0])
nums = [str(num) for pair in min_pair for num in pair]
print(' '.join(nums))
                
