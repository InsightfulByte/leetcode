class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
            
            if nums[i]==candidate:
                count+=1

            if nums[i]!=candidate:
                count-=1
        return candidate 
            
            
        