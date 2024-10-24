class Solution(object):
    def plusOne(self, digits):
        var=0
        for d in range(len(digits), 0, -1):
            if d == 0:
                var+=digits[len(digits) - d]
                continue
            else: 
                var+=digits[len(digits) - d] * (10**(d-1))
        var+=1
        var = str(var)
        res = []
        for r in range(len(var)):
            res.append(int(var[r]))
        return res