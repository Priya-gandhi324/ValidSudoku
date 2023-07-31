from collections import defaultdict

def isValidSudoku(board):
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == "." or board[r][c] == 0:
                continue

            if (board[r][c] in rows[r] and board[r][c] in cols[c] and board[r][c] in boxes[(r//3, c//3)]):
                return False

            rows[r].add(board[r][c])
            cols[c].add(board[r][c])
            boxes[(r//3, c//3)].add(board[r][c])
    
    return True

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board))