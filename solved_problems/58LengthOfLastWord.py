class Solution(object):
    def lengthOfLastWord(self, s):
        a = s.split()
        s = s.replace(" ", "")
        return len(s) - s.rfind(a[-1])