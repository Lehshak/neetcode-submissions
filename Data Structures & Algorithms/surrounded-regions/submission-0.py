from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # step 1 find every border

        borders = []
        # tuple r,c
        rows, cols = len(board), len(board[0])

        for c in range(cols):
            #top & bottom rows
            borders.append((0,c))
            borders.append((rows-1,c))

        for r in range(1, rows-1):
            # right & left excluding the top and bottom intersections
            borders.append((r, 0))
            borders.append((r, cols-1))

        DIR = [(1,0), (-1,0), (0,1), (0,-1)]

        border_regions = set(borders)

        # have to use BFS on borders
        q = deque(borders)
        while q:

            r, c = q.popleft()

            if board[r][c] == "O":
                for dr, dc in DIR:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr,nc) not in border_regions and board[nr][nc] == "O":
                            border_regions.add((nr,nc))
                            q.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in border_regions:
                    board[r][c] = "X"

            



        

        

        



            


        

        