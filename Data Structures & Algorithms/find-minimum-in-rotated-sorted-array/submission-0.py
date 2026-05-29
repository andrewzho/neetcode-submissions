class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0 , len(nums)-1

        while l <= r:
            # in the case where the left side is smaller which means sorted
            if nums[l] < nums[r]:
                return min(res, nums[l])
                break
            #find mid point
            m = (l+r)//2
            #comapre with "smallest" value
            res = min(res, nums[m])
            print(nums[m])
            # if midpoint value is greater than the left most
            if nums[m] >= nums[l]:
                l = m+1
            # if midpoint value is less than left then we move right
            else:
                r = m-1
            
        return res
            
        