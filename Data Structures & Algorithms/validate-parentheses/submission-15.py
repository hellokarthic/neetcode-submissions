class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        # for c in s:
        #     if c in hmap:
        #         if not stack or stack[-1] != hmap[c]:
        #             return False
        #         stack.pop()
        #     else:
        #         stack.append(c)
        # return stack == []
            
            

        for c in s:
            if c in hmap:
                if not stack or stack[-1] != hmap[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return stack == []
            