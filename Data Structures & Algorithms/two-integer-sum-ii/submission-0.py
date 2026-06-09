class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i,n in enumerate(numbers):
            l=i+1
            r=len(numbers)-1
            comp = target-numbers[i]
            while l<=r:
                m = (l+r)//2
                if comp < numbers[m]:
                    r = m-1
                elif comp > numbers[m]:
                    l = m+1
                else:
                    return [(i+1), (m+1)]        

        