# Given an m x n grid of characters board and a string
# word, return true if word exists in the grid.
#
# The word can be constructed from letters of sequentially
# adjacent cells, where adjacent cells are horizontally or
# vertically neighboring. The same letter cell may not be
# used more than once.

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        lw = len(word)

        found = False
        visited = set()
        def backtrack(i, j):
            nonlocal found

            lv = len(visited)
            if lv == lw:
                found = True
                return
            
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + direction[0], j + direction[1]
                if (ni, nj) in visited:
                    continue
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[lv]:
                    visited.add((ni, nj))
                    backtrack(ni, nj)
                    visited.remove((ni, nj))
        
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    visited.add((i, j))
                    backtrack(i, j)
                    visited.remove((i, j))
                    if found:
                        return True
        return False
