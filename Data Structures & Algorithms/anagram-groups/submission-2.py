class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for word in strs:
            hmap.setdefault("".join(sorted(word)),[]).append(word)
        return list(hmap.values())