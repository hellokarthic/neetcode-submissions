class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        print(stones)
        while len(stones)-1 >= 1:
            x = stones[0]
            y = stones[1]
            if x > y:
                stones.remove(x)
                stones[0] = x - y
                stones.sort(reverse=True)
            elif x == y:
                stones.remove(x)
                stones.remove(y)
                stones.sort(reverse=True)
            else:
                stones.remove(y)
                stones[0] = x - y
                stones.sort(reverse=True)
        if len(stones) == 0:
            return 0
        return stones[0] 
