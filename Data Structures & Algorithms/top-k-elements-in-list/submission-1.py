class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hmap = {}
        # freq = [[] for i in range(len(nums) + 1)]
        # res = []
        # for num in nums:
        # 	hmap[num] = 1 + hmap.get(num, 0)
        # for num, count in hmap.items():
        # 	freq[count].append(num)
        # for n in range(len(freq)-1, 0, -1):
        #     for x in freq[n]:
        #         res.append(x)
        #         if len(res) == k:
        #             return res
        heap = []
        hmap = {}
        ans = []
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
        for value, count in hmap.items():
            heapq.heappush(heap, (count, value))
            if len(heap) > k:
                heapq.heappop(heap)
        print("heap", heap)
        print("hashmap", hmap)
        for x in heap:
            ans.append(x[1])
        return ans





