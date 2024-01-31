class Solution:
    def totalNQueens(self, n: int) -> int:
        grid=[[0]*n for _ in range(n)]
        c=[0]
        def valid(i,j,n,grid):
            x=i
            y=j
            while(x>=0):
                if grid[x][y]:
                    return 0
                x-=1
            x=i
            y=j
            while(x>=0 and y>=0):
                if grid[x][y]:
                    return 0
                x-=1
                y-=1
            x=i
            y=j
            while(x>=0 and y<n):
                if grid[x][y]:
                    return 0
                x-=1
                y+=1
            return 1
        def fun(i,n,grid):
            if i==n:
                c[0]+=1
                return
            for j in range(n):
                if valid(i,j,n,grid):
                    grid[i][j]=1
                    fun(i+1,n,grid)
                    grid[i][j]=0
                    
        fun(0,n,grid)
        return c[0]
        