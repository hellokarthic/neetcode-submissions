class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for f in range(len(nums)):
            if f > 0 and nums[f] == nums[f-1]:
                continue
            l, r = f+1, len(nums)-1
            while l < r:
                sum = nums[f] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[f], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: l += 1
                    while l < r and nums[r] == nums[r+1]: r -= 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return res


