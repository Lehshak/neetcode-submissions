class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        DIR = [(1,0), (-1,0), (0,1), (0,-1)]
        reaches_both = []

        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])

        pacific_border = []
        for c in range(cols):
            pacific_border.append((0,c))
        for r in range(1, rows):
            pacific_border.append((r, 0))

        atlantic_border = []
        for c in range(cols):
            atlantic_border.append((rows-1, c))
        for r in range(rows-2, -1, -1):
            atlantic_border.append((r, cols-1))

        def dfs_pacific(r,c):
            curr_height = heights[r][c]
            pacific.add((r,c))

            for dr, dc in DIR:
                nr,nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= curr_height:
                    if (nr,nc) not in pacific:
                        dfs_pacific(nr,nc)

        def dfs_atlantic(r,c):
            curr_height = heights[r][c]
            atlantic.add((r,c))

            for dr, dc in DIR:
                nr,nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= curr_height:
                    if (nr,nc) not in atlantic:
                        dfs_atlantic(nr,nc)

        for r,c in pacific_border:
            if (r,c) not in pacific:
                dfs_pacific(r,c)

        for r,c in atlantic_border:
            if (r,c) not in atlantic:
                dfs_atlantic(r,c)

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    reaches_both.append([r,c])

        return reaches_both




        