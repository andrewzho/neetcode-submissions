class Solution:
    def isValid(self, s: str) -> bool:
        parentSet = []
        openParen = "({["
        closeParen = "]})"
        for i in s:
            print(i, openParen[0],openParen[1], openParen[2])
            if i == openParen[0]:
                parentSet.append(')')
            elif i == openParen[1]:
                parentSet.append('}')
            elif i == openParen[2]:
                parentSet.append(']')
            elif i in closeParen and parentSet:
                if i != parentSet[-1]:
                    return False
                parentSet = parentSet[0:-1]
            elif i in closeParen and not parentSet:
                return False
            else:
                pass
        
        if parentSet == []:
            return True
        
        return False