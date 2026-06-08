class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)
        pre_comp = [1] * len(nums)

        for i in range(0, len(nums)):
            if i !=0:
                res[i] = pre_comp[i-1]
                pre_comp[i] = pre_comp[i-1]   
            pre_comp[i] = pre_comp[i] * nums[i]   
            for j in range(i+1, len(nums)):
                res[i] = res[i] * nums[j]
                j+=1                
            i+=1

        return res         