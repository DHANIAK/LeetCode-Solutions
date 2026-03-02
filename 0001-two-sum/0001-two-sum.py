class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            if target-num in seen:
                return[seen[target-num],i]
            seen[num]=i
solution=Solution()            
nums=[2,7,11,15]
target=9
result = solution.twoSum(nums, target)
print(result)    
               
        