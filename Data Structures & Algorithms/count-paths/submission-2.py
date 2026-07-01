class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def getpos(r, c):
            return f"{r},{c}"
        
        def getneighbours(r, c, m, n):
            rows = [0, 1]
            cols = [1, 0]
            nei = []

            for i in range(2):
                if 0 <= r + rows[i] < m and 0 <= c + cols[i] < n:
                    nei.append((r + rows[i], c + cols[i]))
            return nei

        def dfs(visited, r, c, m, n, memo):

            if r == m - 1 and c == n - 1:
                memo[getpos(r,c)] = 1
                return 1

            cnt = 0
            for nr, nc in getneighbours(r, c, m, n):
                n_pos = getpos(nr, nc)
                if n_pos in memo:
                    cnt += memo[n_pos]

                elif n_pos not in visited:
                    visited.add(n_pos)
                    cnt += dfs(visited, nr, nc, m, n, memo)
                    visited.remove(n_pos)

            memo[getpos(r, c)] = cnt
            return cnt

        visited = set()
        visited.add(getpos(0, 0))
        memo = {}
        return dfs(visited, 0, 0, m, n, memo)
