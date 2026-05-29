class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound, lower_bound = max(piles), 1
        res = upper_bound
        while lower_bound <= upper_bound:
            mid = (upper_bound + lower_bound) // 2

            val = 0
            for i in piles:
                val += math.ceil(float(i)/mid)
            
            if val <= h:
                res = mid
                upper_bound =mid-1
            else:
                lower_bound = mid + 1
        
        return res
        