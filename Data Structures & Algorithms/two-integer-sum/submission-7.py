class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i, n in enumerate(nums):
            if not hash or n not in hash:
                hash[n] = i 
            if (target-n) in hash and hash[(target-n)] != i:
                if (i < hash[(target-n)]):
                    return [i, hash[(target-n)]]
                else:
                    return [hash[(target-n)], i] 
        