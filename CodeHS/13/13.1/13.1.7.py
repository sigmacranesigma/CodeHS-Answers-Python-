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

# Step 2: Use assignment statements to set elements to 1 in an alternating pattern
for row in range(8):
    number = row % 2  # Start with 0 or 1 depending on row
    for col in range(8):  
        if number == 0:
            grid[row][col] = 0
        else:
            grid[row][col] = 1
        number = 1 - number  # Flip between 0 and 1

print_board(grid)
