class Solution(object):
    def twoSum(self, nums, target):
        for num in range(len(nums)):
            for n in range(num+1, len(nums)):
                if nums[num] + nums[n] == target:
                    return [num, n]
        return []