class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sampleSet = set()
        for i in nums:
            if i not in sampleSet:
                sampleSet.add(i)
            else:
                return True
        return False
        