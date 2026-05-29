class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_dict.keys():
                return[num_dict[remainder], i]
            else:
                num_dict[nums[i]] = i
            
        