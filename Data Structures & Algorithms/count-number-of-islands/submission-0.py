class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        DIR = [(1,0), (-1,0), (0,-1), (0,1)]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c] == "0":
                return

            visited.add((r,c))

            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands
