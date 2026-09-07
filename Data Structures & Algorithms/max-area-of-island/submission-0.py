class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        DIR = [(1,0), (-1,0), (0,-1), (0,1)]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c] == 0:
                return 0

            visited.add((r,c))
            # grid is 1 grid
            area = 1

            for dr, dc in DIR:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    area += dfs(nr,nc)

            return area

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == 1:
                    max_area = max(dfs(r,c), max_area)
        return max_area