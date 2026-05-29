class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = 0
        num_dict = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_dict.keys():
                start = num_dict[remainder]
                end = i
                break
            else:
                num_dict[nums[i]] = i 

        return [start, end]
            
        