class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        print(sorted_nums)
        max_value = 0
        count = 0
        temp = -100
        for num in sorted_nums:
            next_num = temp+1
            print(num, next_num, count)
            if num == next_num:
                print('flow a')
                count +=1
            elif num == temp:
                print('flow b')
                pass
            else:
                count += 1
                max_value = max(max_value, count)
                count = 0
            
            temp = num
            max_value = max(max_value, count+1)
        return max_value 

        