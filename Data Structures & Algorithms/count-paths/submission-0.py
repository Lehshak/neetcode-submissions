class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # start point is 

        memo = {}

        def rec(row, col):
            if row == m and col == n:
                return 1
            elif row > m or col > n:
                return 0
                # invalid path

            state = (row,col)
            if (row,col) in memo:
                return memo[(row,col)]

            down = rec(row+1, col)
            right = rec(row, col+1)

            memo[(row,col)] = down + right

            return down+right

        return rec(1,1)


            