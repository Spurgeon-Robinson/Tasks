# This progrtam is a 5x5 Minesweeper game.
# each "#" represents a mine and each "-" represents an empty cell.
# The game initializes a grid with a specified number
# of mines and calculates the numbers
# around each cell, indicating how many mines are adjacent to it.

# The starting grid with mines and empty cells
grid_mine = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]]


def calculate_mines(grid):
    '''Calculates the number of mines around each cell in the grid.'''
    rows = len(grid)
    cols = len(grid[0])
    # Initialize the result grid with zeros
    result = [["0" for _ in range(cols)] for _ in range(rows)]
    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "#":
                result[i][j] = "#"
            else:
                mine_count = 0
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        if grid[x][y] == "#":
                            mine_count += 1
                result[i][j] = str(mine_count)
    # Return the grid with mine counts
    return result


def print_grid(grid):
    '''Prints the grid in a readable format.'''
    for row in grid:
        print(" ".join(row))


# Calculate the mine counts around each cell
mine_count_grid = calculate_mines(grid_mine)

# Print the original grid and the mine count grid
print("Original Grid:")
print_grid(grid_mine)
print("\nMine Count Grid:")
print_grid(mine_count_grid)
