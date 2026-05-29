class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.lower()
        head, tail = 0, len(s) - 1

        while head <= tail:
            if not (('a' <= lowered[head] <= 'z') or ('0' <= lowered[head] <= '9')):
                head += 1
            elif not (('a' <= lowered[tail] <= 'z') or ('0' <= lowered[tail] <= '9')):
                tail -= 1
            else:
                if lowered[head] != lowered[tail]:
                    return False
                head += 1
                tail -= 1
        
        return True
