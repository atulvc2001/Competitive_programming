# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         cols = collections.defaultdict(set)
#         rows = collections.defaultdict(set)
#         squares = collections.defaultdict(set)

#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == ".":
#                     continue
#                 if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[( r // 3, c // 3 )]):
#                     return False
#                 cols[c].add(board[r][c])
#                 rows[r].add(board[r][c])
#                 squares[( r // 3, c // 3 )].add(board[r][c])
#         return True

# the above answer is from neetcode, the difference between the two solutions is that neetcode checks if the element is present or not in the square key instead of iterating through an entire sub square. 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        for i in range(9):
            row = set()
            col = set()
            box = set()
            for j in range(9):
                # Check rows
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
                # Check columns
                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                # Check sub-boxes
                box_row = 3 * (i // 3) + j // 3
                box_col = 3 * (i % 3) + j % 3
                if board[box_row][box_col] != ".":
                    if board[box_row][box_col] in box:
                        return False
                    box.add(board[box_row][box_col])
        return True



