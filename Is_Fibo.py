class Solution(object):
    def isFibo(self, num):
        if num == 0 or num == 1:
            return True
        else:
            is_fibo = False
        seq = [0, 1]
        while seq[-1] + seq[-2] <= num:
            t_sum = seq[-1] + seq[-2]
            seq.append(t_sum)
            # print(seq)
            if num in seq:
                is_fibo = True
                break
        return is_fibo
    
if __name__ == "__main__":
    m = int(input().strip())
    sln = Solution()
    for i in range(m):
        num = int(input().strip())
        if (sln.isFibo(num)):
            print('IsFibo')
        else:
            print('IsNotFibo')