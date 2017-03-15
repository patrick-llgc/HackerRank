class Solution(object):
    def find_max_serving(self, m):
        return (m//2) * (m - m//2)
    
    
if __name__ == "__main__":
    T = int(input().strip())
    s = Solution()
    for i in range(T):
        num = int(input().strip())
        n_servings = s.find_max_serving(num)
        print(n_servings)
    