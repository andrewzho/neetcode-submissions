class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]+', '', s).lower()
        start = 0 
        end = len(s) - 1
        mid = end // 2 

        while (True and s):
            if (start > end) or (start == mid and len(s) % 2 == 1) :
                return True
            if s[start] != s[end]:
                print(s[start], s[end])
                return False
            start += 1
            end -= 1
        
        return True
        