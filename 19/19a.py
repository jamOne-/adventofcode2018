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


def solve(puzzle_input):
  lines = [line.strip() for line in puzzle_input]
  ip_register = int(lines[0].split(' ')[1])
  instructions = lines[1:]
  registers = [0] * 6

  while registers[ip_register] < len(instructions):
    instruction = instructions[registers[ip_register]]
    op_code, *abc = instruction.split(' ')
    a, b, c = tuple(map(int, abc))

    registers[c] = OPERATIONS[op_code](a, b, c, registers)
    registers[ip_register] += 1

  return registers[0]


print(solve(sys.stdin))
