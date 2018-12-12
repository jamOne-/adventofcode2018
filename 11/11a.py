import sys


GRID_SIZE = 300, 300
SQUARE_SIZE = 3


def create_grid(size, grid_serial):
  size_x, size_y = size
  grid = []

  for y in range(1, size_y + 1):
    row = []

    for x in range(1, size_x + 1):
      rack_id = x + 10
      power_level = rack_id * y
      power_level += grid_serial
      power_level *= rack_id
      power_level = power_level % 1000 // 100
      power_level -=5

      row.append(power_level)

    grid.append(row)
  
  return grid


def calculate_square(grid, position):
  x, y = position
  return sum(grid[y][x:x + SQUARE_SIZE] + grid[y + 1][x:x + SQUARE_SIZE] + grid[y + 2][x:x + SQUARE_SIZE])


def solve(grid_serial):
  grid = create_grid(GRID_SIZE, grid_serial)
  best_pos, best_score = None, 0

  for y in range(GRID_SIZE[1] - SQUARE_SIZE):
    for x in range(GRID_SIZE[0] - SQUARE_SIZE):
      square_score = calculate_square(grid, (x, y))

      if square_score > best_score:
        best_score = square_score
        best_pos = x + 1, y + 1

  return best_pos


print(solve(int(sys.stdin.readline().strip())))
