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
  matching = []

  for key, operation in OPERATIONS.items():
    registers = list(before)
    perform_operation(operation, instruction, registers)

    if registers == after:
      matching.append(key)
  
  return matching


def reduce_codes(codes):
  calculated_codes = dict()

  while len(calculated_codes) < 16:
    for code, ops in codes.items():
      rest = ops.difference(set(calculated_codes.values()))

      if len(rest) == 1:
        op = list(rest)[0]
        calculated_codes[code] = op
  
  return calculated_codes


def solve(puzzle_input):
  lines = list(puzzle_input)
  line_i = 0
  codes = { code: set(OPERATIONS.keys()) for code in range(16) }

  while lines[line_i].startswith('Before'):
    before = find_numbers(lines[line_i])
    instruction = find_numbers(lines[line_i + 1])
    after = find_numbers(lines[line_i + 2])
    line_i += 4

    matching_keys = matching_operations(before, instruction, after)
    codes[instruction[0]].intersection_update(set(matching_keys))
  
  codes = reduce_codes(codes)

  line_i += 2
  registers = [0, 0, 0, 0]

  while line_i < len(lines):
    instruction = find_numbers(lines[line_i])
    op_code = instruction[0]
    perform_operation(OPERATIONS[codes[op_code]], instruction, registers)

    line_i += 1
  
  return registers[0]


print(solve(sys.stdin))
