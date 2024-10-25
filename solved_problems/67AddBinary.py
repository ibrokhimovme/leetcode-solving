class Solution(object):
    def addBinary(self, a, b):
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        result = ''
        carry = 0
        for i in range(max_len - 1, -1, -1):
            bit_sum = carry + int(a[i]) + int(b[i])
            result = str(bit_sum % 2) + result
            carry = bit_sum // 2
        if carry:
            result = '1' + result

        return result