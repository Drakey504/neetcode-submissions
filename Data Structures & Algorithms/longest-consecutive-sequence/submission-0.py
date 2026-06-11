class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nset = set(nums)
        cnt = 0

        for n in nums:
            
            i = 1 
            while (n+i) in nset:
                i+=1

            if i > cnt:
                cnt = i

        return cnt             