class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        bs = [set() for i in range(9)]
        cs = [set() for i in range(9)]
        for i in range(len(board)):
            rs = set()
            for j in range(len(board[i])):
                # check row
                val = board[i][j]
                if val not in rs:
                    rs.add(val)
                elif val in rs and val != ".":
                    print(val, i , j)
                    return False
                #check column
                if j == 3:
                    print(cs[j])
                if val not in cs[j]:
                    cs[j].add(val)
                elif val in cs[j] and val != ".":
                    return False

                #check square
                if val in bs[(i//3)*3+j//3] and val != ".":
                    return False
                else:
                    bs[(i//3)+j//3].add(val)
        
        return True
# [".",".","4",".",".",".","6","3","."],
# [".",".",".",".",".",".",".",".","."],
# ["5",".",".",".",".",".",".","9","."],

# [".",".",".","5","6",".",".",".","."],
# ["4",".","3",".",".",".",".",".","1"],
# [".",".",".","7",".",".",".",".","."],

# [".",".",".","5",".",".",".",".","."],
# [".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".","."]]
        