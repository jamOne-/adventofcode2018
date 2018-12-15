import sys


def solve(puzzle_input):
  recipes = '37'
  first, second = 0, 1
  searching_length = len(puzzle_input)

  while recipes[-searching_length:] != puzzle_input:
    if len(recipes) % 100000 == 0:
      print(len(recipes), end='\r', flush=True)

    s = int(recipes[first]) + int(recipes[second])
    a, b = s // 10, s % 10

    if a > 0:
      recipes += str(a)

      if recipes[-searching_length:] == puzzle_input:
        break

    recipes += str(b)

    first = (first + 1 + int(recipes[first])) % len(recipes)
    second = (second + 1 + int(recipes[second])) % len(recipes)

  return len(recipes) - searching_length


print(solve(sys.stdin.readline().strip()))