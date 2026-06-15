class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # countS, countT = {},{}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return countS == countT

        hmap_s = {}
        hmap_t = {}
        for c in s:
            hmap_s[c] = 1 + hmap_s.get(c, 0)
        for c in t:
            hmap_t[c] = 1 + hmap_t.get(c, 0)
        return hmap_s == hmap_t