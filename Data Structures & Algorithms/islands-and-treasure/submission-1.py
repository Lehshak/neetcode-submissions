from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        # bfs
        DIR = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        # we have all treasures
        distance = 1
        visited = set()

        while q:
            
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in DIR:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr,nc) not in visited and grid[nr][nc] == INF:
                            grid[nr][nc] = distance
                            visited.add((nr,nc))
                            q.append((nr,nc))

            distance += 1

        



            




        