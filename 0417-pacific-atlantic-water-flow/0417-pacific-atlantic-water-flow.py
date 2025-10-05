class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row , col = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def fun(r, c, ocean, prev):
            if (r,c) in ocean or r < 0 or c < 0 or r == row or c == col or heights[r][c] < prev:
                return
            ocean.add((r,c))
            fun(r+1, c, ocean, heights[r][c])
            fun(r-1, c, ocean, heights[r][c])
            fun(r, c+1, ocean, heights[r][c])
            fun(r, c-1, ocean, heights[r][c])
            return
            
            
        for c in range(col):
            fun(0, c, pac, heights[0][c])
            fun(row - 1, c, atl, heights[row-1][c])
            
        for r in range(row):
            fun(r, 0, pac, heights[r][0])
            fun(r, col - 1, atl, heights[r][col-1])
        
        return list(pac & atl)
        