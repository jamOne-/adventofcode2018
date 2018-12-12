import sys


GRID_SIZE = 300
MAX_SQUARE_SIZE = 20


def create_grid(size, grid_serial):
  size_x, size_y = size, size
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


def calculate_square(grid, square_size, position):
  pos_x, pos_y = position
  result = 0

  for x in range(pos_x, pos_x + square_size):
    for y in range(pos_y, pos_y + square_size):
      result += grid[y][x]
  
  return result


def update_square_score(grid, square_size, position, square_score):
  x, y = position

  for y in range(y, y + square_size):
    square_score += grid[y][x + square_size - 1] - grid[y][x - 1]

  return square_score


def find_best_position(grid, square_size):
  best_pos, best_score = None, -999999

  for y in range(GRID_SIZE - square_size):
    square_score = calculate_square(grid, square_size, (0, y))

    for x in range(GRID_SIZE - square_size):
      if x != 0:
        square_score = update_square_score(grid, square_size, (x, y), square_score)
      
      if square_score > best_score:
        best_pos, best_score = (x, y), square_score
  
  return best_pos, best_score


def solve(grid_serial):
  grid = create_grid(GRID_SIZE, grid_serial)
  best_pos, best_score, size = None, -999999, 2

  for square_size in range(3, MAX_SQUARE_SIZE + 1):
    pos, score = find_best_position(grid, square_size)
    
    print(square_size, score, pos, end='\r', flush=True)

    if score > best_score:
      best_pos, best_score, size = pos, score, square_size
  
  print(' ' * 40, end='\r')
  return best_pos[0] + 1, best_pos[1] + 1, size


print(solve(int(sys.stdin.readline().strip())))
