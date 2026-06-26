class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        initial_zeroes = []

        rows = len(matrix)
        cols = len(matrix[0])

        # get all 0's O(n*m)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    initial_zeroes.append((i, j))

        if len(initial_zeroes) == 0:
            return
        
        while len(initial_zeroes) > 0:
            r, c = initial_zeroes.pop()

            for i in range(cols):
                matrix[r][i] = 0

            for i in range(rows):
                matrix[i][c] = 0

        return
