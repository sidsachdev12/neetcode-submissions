from typing import Optional

class Node:
    def __init__(self, val: Optional[int], next:list[Optional[Node]]):
        self.val = val
        self.next = next

class Graph:
    def __init__(self):
        # Each vertex value will be a unique integer.
        self.nodes = {}

    def _nodeExist(self, node: int) -> bool:
        return node in self.nodes

    def addEdge(self, src: int, dst: int):

        if not self._nodeExist(src):
            self.nodes[src] = Node(src, [])

        if not self._nodeExist(dst):
            self.nodes[dst] = Node(dst, [])
        
        self.nodes[src].next.append(self.nodes[dst])

    def removeEdge(self, src, dst) -> bool:

        if not (self._nodeExist(src) and self._nodeExist(dst)):
            return False

        src_node = self.nodes[src]
        
        for n in src_node.next:
            if n.val == dst:
                src_node.next.remove(n)
                return True
        
        return False

    def hasPath(self, src, dst) -> bool:

        def dfs(root, visited):

            if root.val == dst:
                return True

            if len(root.next) == 0:
                return False

            visited.add(root)

            for n in root.next:
                if n not in visited:
                    if dfs(n, visited):
                        return True

            return False

        visited = set()

        # for key, value in self.nodes.items():
        #     if len(value.next) == 0:
        #         print(f"{key}, None")
        #     else:
        #         for n in value.next:
        #             print(f"{key}, {n.val}")

        return dfs(self.nodes[src], visited)

