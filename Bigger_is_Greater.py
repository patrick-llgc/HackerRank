class Solution(object):
    def find_min_greater_anagram(self, foo):
        """Find a lexicographically gereater anagram for the input string"""
        # convert letters to ascii array
        ord_array = [ord(letter) for letter in list(foo)]
        diffs = [(ord_array[i] - ord_array[i-1]) for i in range(1, len(ord_array))]
        # find the first pair of neighboring letters in increasing order
        loc = -1
        for i in range(len(diffs)):
            # search in reverse order
            t_loc = len(diffs) - 1 - i
            if diffs[t_loc] > 0:
                loc = t_loc
                break
        if loc < 0:
            return 'no answer'
        else:
            # need to shuffle ord_array[loc:]
            ord_array_slice = sorted(ord_array[loc:])
            for i, num in enumerate(ord_array_slice):
                if num > ord_array[loc]:
                    del(ord_array_slice[i])
                    ord_array_slice.insert(0, num)
                    break
            # replace shuffled slice
            ord_array[loc:] = ord_array_slice
            # convert back to list of chars
            chr_array = [chr(i) for i in ord_array]
            return ''.join(chr_array)
        
if __name__ == "__main__":
    sln = Solution()
    m = int(input().strip())
    for i in range(m):
        foo = input().strip()
        print(sln.find_min_greater_anagram(foo))