from collections import deque

class Node:
  def __init__(self, value = None):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None

def heapify(node):
  smallest = node
  if node.left is not None and node.left.value < smallest.value:
    smallest = node.left
  if node.right is not None and node.right.value < smallest.value:
    smallest = node.right

  if smallest is not node:
    node.value, smallest.value = smallest.value, node.value
    heapify(smallest)

def sort(vals): 
  stack = deque()
  queue = deque()
  
  testlen = len(vals)

  root = Node(vals[0])
  current = root

  # build level order tree
  for num in vals[1:]:
    n = Node(num)

    if current.left is not None and current.right is not None:
      stack.appendleft(current)
      current = queue.popleft()

    if current.left is None:
      current.left = n
      n.parent = current
    elif current.right is None:
      current.right = n
      n.parent = current

    # add the new node to the queue so we can give it children later
    queue.append(n)

  stack.appendleft(current) 
  # remove childless nodes from the queue
  while len(queue) > 0:
    stack.appendleft(queue.popleft())

  assert len(queue) == 0
  assert len(stack) == testlen

  # heapify in reverse level order
  for node in stack:
    heapify(node)
    queue.append(node)

  # queue now holds heap nodes in reverse level order
  assert len(queue) == testlen

  outlist = []

  # heap property now holds. now rebuild the vals list in order
  while True: # fuck it
    outlist.append(root.value)
    n = queue.popleft()
    # n should be a childless node at this point
    assert n.left is None and n.right is None
    root.value = n.value

    if n.parent is None:
      return outlist

    if n.parent.left is n:
      n.parent.left = None
    elif n.parent.right is n:
      n.parent.right = None
    else:
      raise Exception

    heapify(root)

if __name__ == "__main__":
  array = [5, 4, 3, 2, 1]
  # with f as open(sys.argv[1], 'r'):
    # for token in f.read().split():
      # array.append(int(token))

  print(sort(array))
