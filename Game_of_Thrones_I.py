class Solution(object):
    def is_anagram_of_palindrome(self, foo):
        """Tell if a input string is an anagram of a palindrome"""
        letter_dict = {}
        for letter in foo:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
        counts = [(count % 2) for count in letter_dict.values()]
        # if there is only 1 or 0 letters that cannot be paired
        # then it is an anagram of a palindrom
        return (sum(counts) <= 1)

if __name__ == '__main__':
    string = input().strip()
    if Solution().is_anagram_of_palindrome(string):
        print('YES')
    else:
        print('NO')
