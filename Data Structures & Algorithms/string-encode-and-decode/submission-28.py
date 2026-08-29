class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += "№" + s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        strs = s[1:].split("№")
        return strs