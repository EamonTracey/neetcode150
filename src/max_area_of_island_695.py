# You are given an m x n binary matrix grid. An island
# is a group of 1's (representing land) connected 4-directionally
# (horizontal or vertical.) You may assume all four edges of the
# grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in
# the island.
#
# Return the maximum area of an island in grid. If there is no
# island, return 0.

class Solution:
    def neighbors(self, coord: Tuple[int, int], m: int, n: int) -> List[Tuple[int, int]]:
        neighs = []

        for direction in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_coord = (coord[0] + direction[0], coord[1] + direction[1])
            if 0 <= new_coord[0] < m and 0 <= new_coord[1] < n:
                neighs.append(new_coord)

        return neighs

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        max_area = 0
        seen = set()
        for i in range(m):
            for j in range(n):
                if (i, j) == 0 or (i, j) in seen:
                    continue
                
                area = 0
                frontier = [(i, j)]
                while frontier:
                    k, l = frontier.pop()
                    if (k, l) in seen or grid[k][l] == 0:
                        continue
                    seen.add((k, l))
                    area += 1
                    frontier.extend(self.neighbors((k, l), m, n))
                max_area = max(max_area, area)
                
        return max_area

