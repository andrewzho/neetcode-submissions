class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict = defaultdict(int)
        for i in nums:
            frequency_dict[i] += 1
        frequency_list=frequency_dict.items()
        sorted_frequency_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)
        return [i[0] for i in sorted_frequency_list[0:k]]
        