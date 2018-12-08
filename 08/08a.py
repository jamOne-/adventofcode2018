import sys
from functools import reduce


class TreeIterator:
  def __init__(self, tree):
    self.index = -1
    self.nodes = [tree]

    for child in tree.children:
      self.nodes = self.nodes + list(child)

  
  def __next__(self):
    self.index += 1

    if self.index >= len(self.nodes):
      raise StopIteration
    else:
      return self.nodes[self.index]


class Node:
  def __init__(self, children, metadata):
    self.children = children
    self.metadata = metadata
  

  def __iter__(self):
    return TreeIterator(self)


def create_tree(data, i):
  child_n = data[i]
  metadata_n = data[i + 1]
  children = []
  metadata = []

  i = i + 2

  for child_i in range(child_n):
    tree, i = create_tree(data, i)
    children.append(tree)
  
  for metadata_i in range(metadata_n):
    metadata.append(data[i])
    i += 1
  
  return Node(children, metadata), i


def solve(line):
  data = list(map(int, line.split(' ')))
  tree, _ = create_tree(data, 0)

  return reduce(lambda total, node: total + sum(node.metadata), tree, 0)


print(solve(sys.stdin.readline().strip()))
