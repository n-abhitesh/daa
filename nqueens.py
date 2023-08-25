def is_safe(board, row, col, n):
    # Check if there's a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens_util(board, row, n):
    if row == n:
        print_board(board, n)
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, n)
            board[row][col] = 0

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solve_nqueens_util(board, 0, n)

def print_board(board, n):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

# Example usage
n = 8
solve_nqueens(n)
