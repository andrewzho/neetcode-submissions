class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1

        while head <= tail:
            val = numbers[head] + numbers[tail]

            if val < target:
                head += 1
            elif val > target:
                tail -= 1
            else:
                # values are euqal
                return [head + 1, tail + 1]

        return []