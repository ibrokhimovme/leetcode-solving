class Solution(object):
    def strStr(self, haystack, needle):
        for a in range(len(haystack)):
            for n in range(len(needle)):
                if haystack[a] == needle[n]:
                    if haystack[a:a+len(needle)] == needle:
                        jvb = a
                        return a
        return -1