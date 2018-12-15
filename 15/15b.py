import os
import sys
import argparse
import colorama
from colorama import Fore, Back, Style
from collections import deque, namedtuple

colorama.init()
parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="debug", action="store_true")
args = parser.parse_args()

WALL = '#'
EMPTY = '.'
ELF = 'E'
GOBLIN = 'G'

INITIAL_HP = 200
GOBLIN_ATTACK_POWER = 3
BOARD_SIZE = None

Unit = namedtuple('Unit', ['enemy', 'position', 'hp'])


def parse_input(puzzle_input):
  board = []
  units = dict()

  for y, line in enumerate(puzzle_input):
    row = ''

    for x, char in enumerate(line.strip()):
      if char == ELF or char == GOBLIN:
        unit = Unit(char == GOBLIN, (x, y), INITIAL_HP)
        units[x, y] = unit
        char = EMPTY
      
      row += char
    
    board.append(row)

  global BOARD_SIZE
  BOARD_SIZE = len(board), len(board[0])
  return board, units


def draw(board, units):
  print('\n\n')

  for y in range(BOARD_SIZE[0]):
    row = ''

    for x in range(BOARD_SIZE[1]):
      if board[y][x] == WALL:
        row += '■'
      elif (x, y) in units:
        row += '⚔️' if units[x, y].enemy else '🧝'
      else:
        row += ' '
    
    print(row)


def get_neighbours(x, y):
  y_size, x_size = BOARD_SIZE

  for x, y in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
    if 0 <= x < x_size and 0 <= y < y_size:
      yield x, y


def get_closest_enemy(board, units, unit):
  queue = deque([(unit.position, None)])
  visited = set([unit.position])

  while queue:
    (x, y), first_move = queue.popleft()

    for x, y in get_neighbours(x, y):
      if (x, y) not in visited and board[y][x] == EMPTY:
        if (x, y) in units:
          if units[x, y].enemy != unit.enemy:
            return units[x, y], first_move
          else:
            continue

        else:
          visited.add((x, y))
          queue.append(((x, y), (first_move or (x, y))))
  
  return None


def get_neighbouring_enemies(units, unit):
  for x, y in get_neighbours(*unit.position):
    if (x, y) in units and units[x, y].enemy != unit.enemy:
      yield units[x, y]


def tick(board, units, elven_attack_power):
  for position in sorted(units.keys(), key=lambda position: (position[1], position[0])):
    if position not in units:
      continue

    unit = units[position]
    closest_enemy = get_closest_enemy(board, units, unit)

    if not closest_enemy:
      continue

    enemy, first_move = closest_enemy

    if first_move:
      unit = Unit(unit.enemy, first_move, unit.hp)
      units[unit.position] = unit
      del units[position]
    
    neighbouring_enemies = list(get_neighbouring_enemies(units, unit))

    if len(neighbouring_enemies) > 0:
      weakest_enemy = min(neighbouring_enemies, key=lambda enemy: enemy.hp)
      weakest_enemy = Unit(weakest_enemy.enemy, weakest_enemy.position, weakest_enemy.hp - (GOBLIN_ATTACK_POWER if unit.enemy else elven_attack_power))

      if weakest_enemy.hp > 0:
        units[weakest_enemy.position] = weakest_enemy
      else:
        if not weakest_enemy.enemy:
          return 'Elf died :('

        del units[weakest_enemy.position]


def play(board, units, elven_attack_power):
  rounds = 0

  while any(map(lambda unit: unit.enemy, units.values())):
    if tick(board, units, elven_attack_power):
      return None

    rounds += 1
    
    if args.debug:
      draw(board, units)

  return rounds - 1, units


def solve(puzzle_input):
  board, original_units = parse_input(puzzle_input)
  elven_attack_power = 3

  while True:
    print('🧝 ⚔️ : {}'.format(elven_attack_power))

    result = play(board, original_units.copy(), elven_attack_power)

    if result:
      rounds, units = result
      return rounds * sum(map(lambda unit: unit.hp, units.values()))

    elven_attack_power += 1


print(solve(sys.stdin))
