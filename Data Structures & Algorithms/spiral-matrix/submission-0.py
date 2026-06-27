class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols
        spiral = []
        visited = set()
        index = [0, 0]

        def coord(r, c):
            return f"{r},{c}"

        def down(index, matrix):
            nonlocal rows
            nonlocal visited
            order = []

            while index[0] < rows:
                c = coord(index[0], index[1])
                
                if c not in visited:
                    order.append(matrix[index[0]][index[1]])
                    visited.add(c)
                    index[0] += 1
                else:
                    break

            index[0] -= 1
            index[1] -= 1
            return order

        def up(index, matrix):
            nonlocal rows
            nonlocal visited
            order = []

            while index[0] >= 0:
                c = coord(index[0], index[1])
                
                if c not in visited:
                    order.append(matrix[index[0]][index[1]])
                    visited.add(c)
                    index[0] -= 1
                else:
                    break

            index[0] += 1
            index[1] += 1
            return order

        def left(index, matrix):

            nonlocal cols
            nonlocal visited
            order = []

            while index[1] >= 0:
                c = coord(index[0], index[1])
               
                if c not in visited:
                    order.append(matrix[index[0]][index[1]])
                    visited.add(c)
                    index[1] -= 1
                else:
                    break

            index[1] += 1
            index[0] -= 1

            return order

        def right(index, matrix):
            
            nonlocal cols
            nonlocal visited
            order = []

            while index[1] < cols:
                c = coord(index[0], index[1])
                
                if c not in visited:
                    order.append(matrix[index[0]][index[1]])
                    visited.add(c)
                    index[1] += 1
                else:
                    break

            index[1] -= 1
            index[0] += 1

            return order

        while len(spiral) < total:
            spiral += right(index, matrix)
            if len(spiral) == total: break
            spiral += down(index, matrix)
            if len(spiral) == total: break
            spiral += left(index, matrix)
            if len(spiral) == total: break
            spiral += up(index, matrix)
            if len(spiral) == total: break

        return spiral