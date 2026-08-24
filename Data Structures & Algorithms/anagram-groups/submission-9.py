class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c)- 97] += 1
            hmap.setdefault(tuple(count),[]).append(str)
        return list(hmap.values())