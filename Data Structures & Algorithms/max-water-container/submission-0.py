class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        head = 0
        tail = len(heights) - 1
        while head < tail:
            max_h = min(heights[head],heights[tail])
            max_water = max(max_water, max_h * (tail-head))
            if heights[head] <= heights[tail]:
                head +=1
            else:
                tail -=1
        return max_water
        