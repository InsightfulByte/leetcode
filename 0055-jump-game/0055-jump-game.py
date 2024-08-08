class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxjump = 0
        n = len(nums)
        for i in range (n):
            if i > maxjump:
                return False
            if (nums[i]+i)>=maxjump:
                maxjump=(nums[i]+i)
            if maxjump>=n-1:
                return True
        
        return False

        