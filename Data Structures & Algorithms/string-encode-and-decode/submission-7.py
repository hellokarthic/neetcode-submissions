class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str in strs:
            encoded_str += str + "&^"
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = []
        res = s.split("&^")
        return res[0:len(res)-1]
        

        
