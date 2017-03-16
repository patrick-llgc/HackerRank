class Solution(object):
    def find_parity(self, nums):
        """Find parity of an input list of numbers, 0 (even) and 1 (odd)"""
        n_inv = 0
        n_nums = len(nums)
        for i in range(n):
            for j in range(n):
                # unique elements, don't have to worry about ==
                if j > i and nums[j] < nums[i]:
                    n_inv += 1
        return (n_inv % 2)

if __name__ == "__main__":
    sln = Solution()
    m = int(input().strip())
    for i in range(m):
        n = int(input().strip())
        arr = [int(a) for a in input().strip().split()]
        if sln.find_parity(arr):
            print('NO')
        else:
            print('YES')
    