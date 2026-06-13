class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += ":#:" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res = s.split(":#:")
        return res[1:]
        