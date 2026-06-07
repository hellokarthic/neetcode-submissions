class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in intervals[1:]:
            lastend = res[-1][1]
            if lastend >= i[0]:
                res[-1][1] = max(lastend, i[1])
            else:
                res.append(i)
        return res
