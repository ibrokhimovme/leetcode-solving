class Solution(object):
    def checkPerfectNumber(self, num):
        perfect_numbers = {6, 28, 496, 8128, 33550336}
        return num in perfect_numbers