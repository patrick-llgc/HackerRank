import sys

class Solution(object):
    def flipping_bits(self, num):
        # convert to binary string
        bin_num = '{}'.format(bin(num))
        # strip the '0b' at the beginning
        list_digits = list(bin_num[2:])
        # padding up to 32 digits
        list_digits = ['0'] * (32 - len(list_digits)) + list_digits    
        # flipping digits
        list_digits = [str(1-int(num)) for num in list_digits]
        new_num = int(''.join(list_digits), 2)
        return new_num
    def flipping_bits2(self, num):
        max_int = (2 ** 32) - 1
        new_num = max_int ^ num
        return new_num
        
        
if __name__ == '__main__':
    fb = Solution()
    N = input().strip()
    N = int(N)
    for inum in range(N):
        num = input().strip()
        num = int(num)
        new_num = fb.flipping_bits2(num)
        print(new_num)
