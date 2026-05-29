class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rVal = []
        nums.sort()

        for i, v in enumerate(nums):
            if v > 0:
                break
            
            if i > 0 and v == nums[i-1]:
                continue

            head = i+1
            tail = len(nums)-1
            while head < tail:
                value = v + nums[head] + nums[tail]
                if value > 0:
                    tail -= 1
                elif value < 0:
                    head += 1
                else:
                    rVal.append([v, nums[head], nums[tail]])
                    head += 1
                    tail -= 1
                    while nums[head] == nums[head-1] and head < tail:
                        head += 1
        
        return rVal
        