import sys
from collections import namedtuple


Node = namedtuple('Node', ['children', 'metadata', 'value'])


def create_tree(data, i):
  child_n = data[i]
  metadata_n = data[i + 1]
  children = []
  metadata = []
  value = 0

  i = i + 2

  for child_i in range(child_n):
    tree, i = create_tree(data, i)
    children.append(tree)
  
  for metadata_i in range(metadata_n):
    metadata.append(data[i])
    i += 1

  if child_n == 0:
    value = sum(metadata)
  else:
    for index in metadata:
      if index <= child_n and index >= 1:
        value += children[index - 1].value
  
  return Node(children, metadata, value), i


def solve(line):
  data = list(map(int, line.split(' ')))
  tree, _ = create_tree(data, 0)

  return tree.value


print(solve(sys.stdin.readline().strip()))
