class Solution(object):
    def singleNumber(self, nums):
        kichik = 100
        num1 = 0
        for num in nums:
            cn = nums.count(num)
            if cn < kichik: 
                kichik = cn
                num1 = num
                
        return num1