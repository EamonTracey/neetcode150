# Given an m x n 2D binary grid grid which represents
# a map of '1's (land) and '0's (water), return the
# number of islands.
#
# An island is surrounded by water and is formed by
# connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all
# surrounded by water.

class Solution:
    def neighbors(self, coord: Tuple[int, int], m: int, n: int) -> List[Tuple[int, int]]:
        neighbors = []
        if coord[0] > 0:
            neighbors.append((coord[0] - 1, coord[1]))
        if coord[0] < m - 1:
            neighbors.append((coord[0] + 1, coord[1]))
        if coord[1] > 0:
            neighbors.append((coord[0], coord[1] - 1))
        if coord[1] < n - 1:
            neighbors.append((coord[0], coord[1] + 1))
        return neighbors

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        n_islands = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                if (i, j) in seen:
                    continue
                n_islands += 1
                frontier = [(i, j)]
                while frontier:
                    node = frontier.pop()
                    if node in seen:
                        continue
                    seen.add(node)
                    for neighbor in self.neighbors(node, m, n):
                        if grid[neighbor[0]][neighbor[1]] == "1":
                            frontier.append(neighbor)
                
        return n_islands

