class NQueens:

    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solution_count = 0

    def is_safe(self, row, col):
        # Check if a queen can be placed at the given position without conflicting with previous queens

        # Check for queens in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check for queens in the upper diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check for queens in the lower diagonal
        i, j = row, col
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def solve_nqueens(self):
        # Recursive function to solve the n-queens problem

        def backtrack(row):
            if row == self.n:
                # Base case: All queens have been placed
                self.solution_count += 1
                self.print_solution()
                return

            for col in range(self.n):
                if self.is_safe(row, col):
                    # Place a queen at the current position
                    self.board[row][col] = 1

                    # Recur for the next row
                    backtrack(row + 1)

                    # Backtrack: Remove the queen from the current position
                    self.board[row][col] = 0

        # Start the backtracking algorithm from the first row
        backtrack(0)

    def print_solution(self):
        # Print the current arrangement of queens on the board
        print(f"Solution {self.solution_count}:")
        for row in self.board:
            print(' '.join(['Q' if cell == 1 else '-' for cell in row]))
        print()


# Test the implementation
n = 8  # Number of queens and board size
queens = NQueens(n)
queens.solve_nqueens()
