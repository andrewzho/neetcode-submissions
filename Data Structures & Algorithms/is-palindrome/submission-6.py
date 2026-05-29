class Solution:
    
    def isPalindrome(self, s: str) -> bool:
        head = 0
        tail = len(s) - 1
        while head < tail:
            print(s[head], s[tail])
            if not self.alphaNum(s[head]):
                head += 1
            elif not self.alphaNum(s[tail]):
                tail -= 1
            elif s[head].lower() != s[tail].lower():
                return False
            else:
                head +=1
                tail -=1
        
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        