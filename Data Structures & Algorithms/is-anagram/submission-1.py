class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HashMap = {}
        for i in s:
            if i not in HashMap:
                HashMap[i] = 1
            else:
                HashMap[i] += 1
        
        for i in t:
            if i not in HashMap:
                return False
            HashMap[i] -= 1
            if HashMap[i] < 0:
                return False
        
        for k,v in HashMap.items():
            if v > 0:
                return False

        return True
        