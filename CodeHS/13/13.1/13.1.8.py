# Pass this function a list of lists, and it will print it such that it looks like the grids in the exercise instructions.
def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))

# Your code here...
# Step 1: Create an 8x8 grid filled with 0s
grid = []
for row in range(8):  # Creating an 8x8 grid filled with 0s
    grid.append([0] * 8)

# Step 2: Set elements in the first 3 rows to alternate between 0 and 1
for row in range(3):
    number = row % 2  # Start with 0 or 1 depending on row
    for col in range(8):
        grid[row][col] = number
        number = 1 - number  # Flip between 0 and 1

# Step 3: Set elements in the next 2 rows to all 0s (no alternation needed)
for row in range(3, 5):
    grid[row] = [0] * 8

# Step 4: Set elements in the last 3 rows to alternate between 0 and 1
for row in range(5, 8):
    number = row % 2  # Start with 0 or 1 depending on row
    for col in range(8):
        if number == 0:
            grid[row][col] = 0
            number = 1 - number  # Flip between 0 and 1
        else: 
            grid[row][col] = number
            number = 1 - number

# Print the grid
print_board(grid)
