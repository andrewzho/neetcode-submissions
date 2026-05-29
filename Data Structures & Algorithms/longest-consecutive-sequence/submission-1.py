class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        maxVal = 0

        for n in ns:
            length = 1
            if (n+1) in ns:
                length += 1
                while(n+length) in ns:
                    length +=1
            maxVal = max(length, maxVal)
        return maxVal


        