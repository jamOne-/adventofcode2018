import sys


def solve(puzzle_input):
  recipes = '37'
  first, second = 0, 1

  while len(recipes) < puzzle_input + 10:
    s = int(recipes[first]) + int(recipes[second])
    a, b = s // 10, s % 10

    if a > 0:
      recipes += str(a)
    
    recipes += str(b)

    first = (first + 1 + int(recipes[first])) % len(recipes)
    second = (second + 1 + int(recipes[second])) % len(recipes)

  return recipes[-10:]


print(solve(int(sys.stdin.readline().strip())))