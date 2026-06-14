class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        max_sum = nums[0]
        if len(nums) == 1:
            return nums[0]
        for n in nums:
            total += n
            max_sum = max(total, max_sum)
            if total < 0:
                total = 0
        return max_sum

