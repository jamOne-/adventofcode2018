import re
import sys


def neighbours(x, y):
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      new_x, new_y = x + dx, y + dy

      if (new_x, new_y) != (x, y):
        yield new_x, new_y


def has_neighbour(taken_positions, point):
  x, y = point

  for x, y in neighbours(x, y):
    if (x, y) in taken_positions:
      return True
  
  return False


def end(points):
  taken_positions = set(map(lambda point: (point[0], point[1]), points))
  
  for x, y, vx, vy in points:
    if not has_neighbour(taken_positions, (x, y)):
      return False
  
  return True


def update_points(points):
  for x, y, vx, vy in points:
    x, y = x + vx, y + vy
    yield x, y, vx, vy


def draw_points(points):
  x_min = min(points, key=lambda point: point[0])[0]
  y_min = min(points, key=lambda point: point[1])[1]
  x_max = max(points, key=lambda point: point[0])[0]
  y_max = max(points, key=lambda point: point[1])[1]

  message = [[' '] * (x_max - x_min + 1) for i in range(y_max - y_min + 1)]

  for x, y, vx, vy in points:
    message[y - y_min][x - x_min] = '#'
  
  for row in message:
    print(''.join(row))


def solve(lines):
  points = []

  for line in lines:
    x, y, vx, vy = map(int, re.findall('-?\d+', line))
    points.append((x, y, vx, vy))
  
  while not end(points):
    points = list(update_points(points))
  
  draw_points(points)


solve(sys.stdin)
