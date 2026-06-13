class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        length = 0
        #check if it's the first occurent of range
        for n in nums:
            if n-1 not in numSet:
                while (n + length) in numSet:
                    length += 1
                longest = max (longest, length)
                length = 0
            else:
                continue                      
        return longest