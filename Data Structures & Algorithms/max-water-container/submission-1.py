class Solution:
    def maxArea(self, heights: List[int]) -> int:
        capacity = []
        left, right = 0, len(heights)-1
        max_area = 0
        while left < right:
            capacity = min(heights[left], heights[right]) * (right-left)
            max_area = max (max_area, capacity)
            if heights[left] <heights[right]:
                left += 1
            else:
                right -=1
        return max_area