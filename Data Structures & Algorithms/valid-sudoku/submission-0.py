class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
 
        for row in board:
            nums = [c for c in row if c != '.']
            if len(nums) != len(set(nums)):
                return False
                

        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != '.']
            if len(nums) != len(set(nums)):
                return False
                

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = [
                    board[i][j]
                    for i in range(r, r + 3)
                    for j in range(c, c + 3)
                    if board[i][j] != '.'
                ]
                if len(nums) != len(set(nums)):
                    return False
                    
        return True