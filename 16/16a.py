import re
import sys


OPERATIONS = {
  'addr': lambda a, b, c, registers: registers[a] + registers[b],
  'addi': lambda a, b, c, registers: registers[a] + b,
  'mulr': lambda a, b, c, registers: registers[a] * registers[b],
  'muli': lambda a, b, c, registers: registers[a] * b,
  'banr': lambda a, b, c, registers: registers[a] & registers[b],
  'bani': lambda a, b, c, registers: registers[a] & b,
  'borr': lambda a, b, c, registers: registers[a] | registers[b],
  'bori': lambda a, b, c, registers: registers[a] | b,
  'setr': lambda a, b, c, registers: registers[a],
  'seti': lambda a, b, c, registers: a,
  'grir': lambda a, b, c, registers: 1 if a > registers[b] else 0,
  'gtri': lambda a, b, c, registers: 1 if registers[a] > b else 0,
  'gtrr': lambda a, b, c, registers: 1 if registers[a] > registers[b] else 0,
  'eqir': lambda a, b, c, registers: 1 if a == registers[b] else 0,
  'eqri': lambda a, b, c, registers: 1 if registers[a] == b else 0,
  'eqrr': lambda a, b, c, registers: 1 if registers[a] == registers[b] else 0
}


def find_numbers(line):
  return list(map(int, re.findall('\d+', line)))


def perform_operation(operation, instruction, registers):
  op_code, a, b, c = instruction
  registers[c] = operation(a, b, c, registers)


def matching_operations(before, instruction, after):
  counter = 0

  for operation in OPERATIONS.values():
    registers = list(before)
    perform_operation(operation, instruction, registers)

    if registers == after:
      counter += 1
  
  return counter


def solve(puzzle_input):
  lines = list(puzzle_input)
  line_i = 0
  result = 0

  while lines[line_i].startswith('Before'):
    before = find_numbers(lines[line_i])
    instruction = find_numbers(lines[line_i + 1])
    after = find_numbers(lines[line_i + 2])
    line_i += 4

    if matching_operations(before, instruction, after) >= 3:
      result += 1
  
  return result


print(solve(sys.stdin))
