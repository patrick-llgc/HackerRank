class Solution():
    def twoSum(self, arr, s):
        """Return indices of the two members producing the required sum"""
        residual_dict = {}
        for i, num in enumerate(arr):
            if (s - num) in residual_dict:
                return([residual_dict[s-num]+1, i+1])
            else:
                residual_dict[num] = i
                
if __name__ == "__main__":
    sln = Solution()
    n_trips = int(input().strip())
    for _ in range(n_trips):
        s = int(input().strip())
        m = int(input().strip())
        arr = [int(num) for num in input().strip().split()]
        result = ' '.join([str(num) for num in sln.twoSum(arr, s)])
        print(result)