class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashMap = {}
        for i in nums:
            if i not in HashMap:
                HashMap[i] = 1
            else:
                HashMap[i] +=1
        HashMap = sorted(HashMap.items(), key= lambda x:x[1], reverse = True)
        RL = []
        for i in range(k):
            RL.append(HashMap[i][0])

        return RL


        