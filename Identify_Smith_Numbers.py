class Solution(object):
    def find_factors(self, num):
        """Return a list of factors for a given input integer."""
        factors = []
        is_not_prime = 1
        t_num = num
        while(is_not_prime):
            is_not_prime = 0
            # note: need to +1 for suqare numbers
            for i in range(2, int(t_num ** 0.5) + 1):
                if (t_num % i) == 0:
                    # print(t_num, i)
                    factors.append(i)
                    is_not_prime = 1
                    t_num = t_num // i
                    break
        if t_num > 1:
            # note: critical! otherwise 1 would be wrongly categorized
            factors.append(t_num)
        return factors

    def is_smith_number(self, num):
        """Return bool of whether a number is a smith number"""
        # remember to sum up digits of factors with more than one digit
        factors = [str(factor) for factor in self.find_factors(num)]
        #print(factors)
        factor_string = ''.join(factors)
        sum_factors = sum([int(digit) for digit in factor_string])
        list_of_digits = list(str(num))
        sum_digits = sum([int(digit) for digit in list_of_digits])
        return (sum_factors == sum_digits)

if __name__ == '__main__':
    foo = int(input().strip())
    if Solution().is_smith_number(foo):
        print(1)
    else:
        print(0)
