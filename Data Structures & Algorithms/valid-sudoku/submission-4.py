class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_dict = defaultdict(set)
        row_dict = defaultdict(set)
        square_dict = defaultdict(set)
        
        for i in range(9):
            row = i // 3
            for j in range(9):
                box = j // 3
                value = board[i][j]
                square_value = str(row)+str(box)
                # check row values
                if value == '.':
                    continue
                if value not in row_dict[i]:
                    row_dict[i].add(value)
                else:
                    return False
                if value not in column_dict[j]:
                    column_dict[j].add(value)
                else:
                    return False
                if value not in square_dict[square_value]:
                    square_dict[square_value].add(value)
                else:
                    return False

        return True