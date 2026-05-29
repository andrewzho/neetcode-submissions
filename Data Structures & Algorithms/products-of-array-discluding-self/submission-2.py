class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        NL = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            NL[i] = prefix
            prefix *= nums[i]
        print(NL)
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            NL[i] *= postfix
            postfix *= nums[i]
        return NL
        