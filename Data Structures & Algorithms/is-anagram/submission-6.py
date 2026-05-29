class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWord = dict()
        for i in s:
            if i in firstWord.keys():
                firstWord[i] += 1
            else:
                firstWord[i] = 1
        for i in t:
            if i in firstWord.keys() and firstWord[i] >= 0:
                firstWord[i] -= 1
            else:
                return False
            if firstWord[i] <= 0:
                firstWord.pop(i)
        return firstWord == dict()
        