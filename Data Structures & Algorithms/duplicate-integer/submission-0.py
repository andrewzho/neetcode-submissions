class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prev = -1
        for i in sorted(nums):
            if i == prev:
                return True
            prev = i
        
        return False
         