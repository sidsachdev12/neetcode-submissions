import math

class MinHeap:
    
  def __init__(self):
    # Implementing a an array
    self.heap = []

  def push(self, val: int) -> None:
    # Add the entry as a leaf
    self.heap.append(val)
    i = len(self.heap) - 1

    # Bubble up if necessary
    parent = math.floor((i-1)/2)

    while parent >= 0 and self.heap[parent] > self.heap[i]:
      tmp = self.heap[i]
      self.heap[i] = self.heap[parent]
      self.heap[parent] = tmp

      i = parent
      parent = math.floor((i-1)/2)

  def pop(self) -> int:
    if len(self.heap) == 0:
      return -1

    ret = self.top()
    leaf = self.heap.pop()

    if len(self.heap) == 0:
      return ret

    # Add leaf as top node
    self.heap[0] = leaf
    parent = 0
    childA = 2*parent + 1
    childB = 2*parent + 2

    child = childA
    if childA < len(self.heap) - 1 and self.heap[childA] > self.heap[childB]:
        child = childB
    
    # Bubble down if necessary
    while child < len(self.heap) and self.heap[parent] > self.heap[child]:
      
        tmp = self.heap[child]
        self.heap[child] = self.heap[parent]
        self.heap[parent] = tmp
        parent = child

        childA = 2*parent + 1
        childB = 2*parent + 2 

        if max(childA, childB) >= len(self.heap):
            break

        child = childA
        if self.heap[childA] > self.heap[childB]:
            child = childB

    return ret

  def top(self) -> int:
    return -1 if len(self.heap) == 0 else self.heap[0]
  
  def print(self) -> None:
    print(self.heap)
      
  def heapify(self, nums: List[int]) -> None:
    self.heap = []

    for n in nums:
        self.push(n)