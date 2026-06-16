class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        res = []
        for i in range(len(nums)):
            left = 1
            right = 1
            for j in range(0,i):
                left *= nums[j]
            for j in range(i+1, len(nums)):
                right *= nums[j]
            total = left * right
            res.append(total)
        return res