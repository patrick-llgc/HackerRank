class Solution(object):
    def max_min(self, arr, k):
        """Find the min span that covers k numbers in input list"""
        arr = sorted(arr)
        diffs = [arr[i] - arr[i-(k-1)] for i in range(k-1, len(arr))]
        return (min(diffs))
        
if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for i in range(n):
        n = int(input().strip())
        arr.append(n)
    print(Solution().max_min(arr, k))
    