from typing import Optional

class Node:
  def __init__(self, val: Optional[int] , next: 'Optional[Node]', prev: 'Optional[Node]') -> None:
    self.val = val
    self.next = next
    self.prev = prev

class Deque:
    
    def __init__(self):
        self.left = Node(None, None, None)
        self.right = self.left

    def isEmpty(self) -> bool:
        return self.left.val == self.right.val == None
        

    def append(self, value: int) -> None:
        new_node = Node(value, None, None)
        if self.isEmpty():
            self.left = new_node
            self.right = new_node
        else:
            prev = self.right
            self.right.next = new_node
            new_node.prev = prev
            self.right = self.right.next
        

    def appendleft(self, value: int) -> None:
        new_node = Node(value, None, None)
        if self.isEmpty():
            self.left = new_node
            self.right = new_node
        else:
            start = self.left
            start.prev = new_node
            new_node.next = start
            self.left = new_node
            print(self.right.prev.val)

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        ret = self.right.val

        if self.right.prev is None:
            self.right = self.left = Node(None, None, None)
        else:
            self.right = self.right.prev
            self.right.next = None
            print(self.right.val, self.right.prev, self.right.next)
        
        return ret

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        ret = self.left.val

        if self.left.next is None:
            self.left = self.right = Node(None, None, None)
        else:
            self.left = self.left.next
            self.left.prev = None

        return ret