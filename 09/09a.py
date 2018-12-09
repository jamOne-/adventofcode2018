import re
import sys


class Marble:
  def __init__(self, value, prev, next):
    self.value, self.prev, self.next = value, prev, next


def move(marble, n):
  if n == 0:
    return marble
  elif n > 0:
    return move(marble.next, n - 1)
  else:
    return move(marble.prev, n + 1)


def solve(line):
  players, highest_marble = map(int, re.findall('\d+', line))
  scores = [0] * players

  circle = Marble(0, None, None)
  circle.prev = circle
  circle.next = circle

  for marble in range(1, highest_marble + 1):
    if marble % 23 == 0:
      removed = move(circle, -7)
      removed.prev.next = removed.next
      removed.next.prev = removed.prev

      circle = removed.next
      current_player = marble % players
      scores[current_player] += marble + removed.value

    else:
      new_marble = Marble(marble, circle.next, circle.next.next)
      new_marble.prev.next = new_marble
      new_marble.next.prev = new_marble
      circle = new_marble

  return max(scores)


print(solve(sys.stdin.readline().strip()))
