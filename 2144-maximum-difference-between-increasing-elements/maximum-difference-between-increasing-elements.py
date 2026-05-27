class Solution:
    def maximumDifference(self, nums):
        min_diff=float('inf')
        max_diff = -1
        for i in range(len(nums)):
            min_diff=min(min_diff,nums[i])

            if nums[i] > min_diff:
                max_diff = max(max_diff,nums[i]-min_diff)
        return max_diff 
        