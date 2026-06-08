class Solution:

    def encode(self, strs: List[str]) -> str:

        if len(strs) == 0:
            return ""

        res = ""
        
        for s in strs:
            res = res + (s)
            res = res + ("\n")

        return res

    def decode(self, s: str) -> List[str]:

        if s == "":
            return []
        s = s[:-1]
        return s.split("\n")