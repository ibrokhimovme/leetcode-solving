class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        chars = [chr(i) for i in range(32, 127) if not chr(i).isalnum()]
        for char in chars:
            s = s.replace(char, "")
        s_reversed = s[::-1]
        if s_reversed == s:
            return True
        else:
            return False