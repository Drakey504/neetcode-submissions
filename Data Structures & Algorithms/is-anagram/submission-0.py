class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ans = True
        for i,j in zip(sorted(s), sorted(t)):
            if i!=j:
                ans=False
                break
        return ans         
