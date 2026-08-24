class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap_s = {}
        hmap_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hmap_s[s[i]] = 1 + hmap_s.get(s[i], 0)
            hmap_t[t[i]] = 1 + hmap_t.get(t[i], 0)
        return hmap_s == hmap_t
