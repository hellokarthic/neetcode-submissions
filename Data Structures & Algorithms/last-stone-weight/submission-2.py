import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for s in stones:
            heap.append(-s)
        heapq.heapify(heap)    
        while len(heap)-1 >= 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x > y:
                heapq.heappush(heap, -(x - y))
            elif x < y:
                heapq.heappush(heap, -(x - y))
        if len(heap) == 0:
            return 0
        return -heap[0]
