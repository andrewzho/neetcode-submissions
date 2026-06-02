class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1] * len(nums)
        output = []

        for i in range(1, len(nums)):
            left.append(int(left[i-1] * nums[i-1]))
            
        for i in range(len(nums)-2, -1, -1):
            right[i] = int(right[i+1]*nums[i+1])
        
        for i in range(len(nums)):
            output.append(left[i] * right[i])

        return output
        