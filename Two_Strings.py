class Solution(object):
    def exist_common(self, a, b):
        set_a = set(list(a))
        common_flag = 0
        for char in b:
            if char in set_a:
                common_flag = 1
                break
        return common_flag

            
if __name__ == "__main__":
    sln = Solution()
    p = int(input().strip())
    for _ in range(p):
        a = input().strip()
        b = input().strip()
        if sln.exist_common(a, b):
            print('YES')
        else:
            print('NO')