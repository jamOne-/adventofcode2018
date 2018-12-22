import re
import sys
import heapq


def get_all_numbers(string):
  return re.findall('\d+', string)


def prepare_cave(target, depth):
  SIZE_OFFSET = 1500
  cols, rows = target[0] + 1 + SIZE_OFFSET, target[1] + 1 + SIZE_OFFSET
  cave = [[0] * (cols) for row in range(rows)]

  for x in range(1, cols):
    cave[0][x] = (x * 16807 + depth) % 20183
  
  for y in range(1, rows):
    cave[y][0] = (y * 48271 + depth) % 20183
  
  for y in range(1, rows):
    for x in range(1, cols):
      cave[y][x] = (cave[y][x - 1] * cave[y - 1][x] + depth) % 20183
  
  cave[0][0] = depth % 20183
  cave[target[1]][target[0]] = depth % 20183

  cave = [list(map(lambda region: region % 3, row)) for row in cave]

  return cave


def get_neighbours(cave, position, equipment):
  x, y = position
  max_x, max_y = len(cave[0]), len(cave)

  for x, y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
    if max_x > x >= 0 and max_y > y >= 0 and cave[y][x] != equipment:
      yield x, y


def fastest_path_time(cave, target):
  initial_state = ((0, 0), 1)
  state_time_dict = dict()
  state_time_dict[initial_state] = 0
  queue = [(0, *initial_state)]

  while queue:
    time, position, equipment = heapq.heappop(queue)

    if state_time_dict[position, equipment] < time:
      continue

    if (position, equipment) == (target, 1):
      return time

    for new_position in get_neighbours(cave, position, equipment):
      new_time = time + 1
      state = new_position, equipment

      if state not in state_time_dict or state_time_dict[state] > new_time:
        state_time_dict[state] = new_time
        heapq.heappush(queue, (new_time, *state))
    
    for new_equipment in [0, 1, 2]:
      new_time = time + 7
      state = position, new_equipment

      if cave[position[1]][position[0]] != new_equipment and (state not in state_time_dict or state_time_dict[state] > new_time):
        state_time_dict[state] = new_time
        heapq.heappush(queue, (new_time, *state))


def solve(puzzle_input):
  lines = list(puzzle_input)
  depth = int(get_all_numbers(lines[0])[0])
  target = tuple(map(int, get_all_numbers(lines[1])))
  cave = prepare_cave(target, depth)

  return fastest_path_time(cave, target)


print(solve(sys.stdin))
