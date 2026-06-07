class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[(ord(c) - ord("a"))] += 1
            hmap.setdefault(tuple(count),[]).append(s)
        return list(hmap.values())
            


        # hmap = {}
        # for word in strs:
        #     hmap.setdefault("".join(sorted(word)),[]).append(word)
        # print(hmap)
        # return list(hmap.values())