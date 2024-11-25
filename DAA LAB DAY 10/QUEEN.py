def solve_n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    solutions = []
    
    def is_safe(row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            if col - (row - i) >= 0 and board[i][col - (row - i)] == 'Q':
                return False
            if col + (row - i) < N and board[i][col + (row - i)] == 'Q':
                return False
        return True

    def solve(row):
        if row == N:
            solutions.append([''.join(board[i]) for i in range(N)])
            return
        for col in range(N):
            if is_safe(row, col):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '.'
    
    solve(0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

# Example visualizations for N = 4, N = 5, and N = 8
print("Solutions for N = 4")
print_solutions(solve_n_queens(4))

print("Solutions for N = 5")
print_solutions(solve_n_queens(5))

print("Solutions for N = 8")
print_solutions(solve_n_queens(8))
