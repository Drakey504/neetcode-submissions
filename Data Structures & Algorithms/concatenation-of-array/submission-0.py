class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2*len(nums))
        for i, val in enumerate(nums):
            ans[i] = val
            ans[i + len(nums)] = val

        return ans

            


        