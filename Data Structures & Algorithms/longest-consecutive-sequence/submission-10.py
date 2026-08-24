class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet = set(nums)
        # longest = 0
        # #check if it's the first occurent of range
        # for n in nums:
        #     if n-1 not in numSet:
        #         length = 0
        #         while (n + length) in numSet:
        #             length += 1
        #         longest = max (longest, length)
        #     else:
        #         continue                      
        # return longest
        max_length = 0
        numSet = set(nums)
        for num in nums:
            if num-1 not in numSet:
                length = 0
                while (num+length) in numSet:
                    length += 1
                max_length = max(length, max_length)
        return max_length