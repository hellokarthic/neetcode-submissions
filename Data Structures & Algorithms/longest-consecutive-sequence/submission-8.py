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
        # max_length = 0
        # numSet = set(nums)
        # for num in nums:
        #     if num-1 not in numSet:
        #         length = 0
        #         while (num+length) in numSet:
        #             length += 1
        #         max_length = max(length, max_length)
        # return max_length
        max_sum = 0
        nums_set = set(nums)
        for num in nums:
            if num -1 in nums_set:
                continue
            else:
                sum = 1
                while num + 1 in nums_set:
                    sum += 1
                    num+=1
                max_sum = max(sum, max_sum)
        return max_sum
