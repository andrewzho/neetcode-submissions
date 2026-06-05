class Solution:
    def number_check(self, val):
        if val >= '0' and val <= '9':
            return True
        else:
            return False

    def character_check(self, val):
        if val >= 'a' and val <= 'z':
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) -1
        s = s.lower()
        while True:
            # check index
            if start > end:
                return True
            
            # setup
            start_val = self.number_check(s[start]) or self.character_check(s[start])
            end_val = self.number_check(s[end]) or self.character_check(s[end])

            # check if valid
            if start_val and end_val:
                pass
            elif not start_val:
                start +=1
                continue
            else:
                end -= 1
                continue
            print(start_val,start, end_val, end)

            # character compare
            if s[start] == s[end]:
                start +=1
                end -= 1
            else:
                return False
            
        return True

        