class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head, tail = 0, len(numbers)-1
        while head < tail:
            print(head, tail)
            if numbers[head] + numbers[tail] == target:
                return [head+1, tail+1]
            else:
                if abs(head - tail) == 1:
                    head += 1
                    tail = len(numbers)-1
                else:
                    tail -= 1
        
        return []

        