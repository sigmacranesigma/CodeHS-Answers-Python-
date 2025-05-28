# made with ai

# Pass this function a list of lists, and it will
# print it such that it looks like the grids in
# the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))

# Your code here...
# Step 1: Create an 8x8 grid filled with 0s
grid = []
for row in range(8):
    grid.append([0] * 8)

# Step 2: Use assignment statements to set elements to 1
for row in range(8):
    if row < 3 or row > 4:
        for col in range(8):
            grid[row][col] = 1  # <-- Explicit assignment

print_board(grid)
