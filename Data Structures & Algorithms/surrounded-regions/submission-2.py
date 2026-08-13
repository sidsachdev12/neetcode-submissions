from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0]) # rows x cols

        # Get position string
        def getpos(i, j) -> tuple:
            return (i,j)
        
        # Get neighs in the 4 directions
        def get_neighbours(r, c):
            nonlocal m
            nonlocal n

            row = [0, 1, 0, -1]
            col = [1, 0, -1, 0]
            nei = []

            for i in range(len(row)):
                if 0 <= r + row[i] < m and  0 <= c + col[i] < n:
                    nei.append((r + row[i], c + col[i]))

            return nei

        def bfs(r, c, visited, safe):
            if getpos(r, c) in visited:
                return

            visited.add(getpos(r, c))
            safe.add(getpos(r, c))

            queue = deque([(r, c)])
            # visited = set()
            # safe = set()

            while queue:
                r, c = queue.popleft()

                for nr, nc in get_neighbours(r, c):
                    pos = getpos(nr, nc)
                    if pos in visited:
                        continue
                    visited.add(pos)
                    if board[nr][nc] == 'X':
                        continue
                    safe.add(pos)
                    queue.append((nr, nc))

        safe, visited = set(), set()
        # top
        for i in range(n):
            if board[0][i] == "O":
                bfs(0, i, visited, safe)
        # left
        for i in range(m):
            if board[i][0] == "O":
                bfs(i, 0, visited, safe)

        # bottom
        for i in range(n):
            if board[m-1][i] == "O":
                bfs(m-1, i, visited, safe)

        # right
        for i in range(m):
            if board[i][n-1] == "O":
                bfs(i, n-1, visited, safe)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and getpos(i,j) not in safe:
                    board[i][j] = "X"
