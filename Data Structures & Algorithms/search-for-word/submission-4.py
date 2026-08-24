class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        total_rows, total_cols = len(board), len(board[0])

        def _get_neighbours(r, c):
            nonlocal total_rows
            nonlocal total_cols

            rows = [0, 1, 0, -1]
            cols = [1, 0, -1, 0]
            neighs = []

            for i in range(4):
                nr, nc = r + rows[i], c + cols[i]

                if 0 <= nr < total_rows and 0 <= nc < total_cols:
                    neighs.append((nr, nc))
            return neighs

        def dfs(r, c, index, visited):
            found = False

            if index == len(word):
                return True
            
            if board[r][c] != word[index]:
                return False

            if (r,c) in visited:
                return False

            visited.add((r,c))


            for nr, nc in _get_neighbours(r, c):                
                found = found or dfs(nr, nc, index+1, visited)
            
            visited.remove((r,c))
            return found

        if total_rows == 1 and total_cols == 1 and board[0][0] == word:
            return True

        for i in range(total_rows):
            for j in range(total_cols):
                if dfs(i, j, 0, set()):
                    return True

        return False


        