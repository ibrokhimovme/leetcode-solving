class Solution(object):
    def search(self, nums, target):
        for num in range(len(nums)):
            if nums[num] == target:
                return num
        return -1