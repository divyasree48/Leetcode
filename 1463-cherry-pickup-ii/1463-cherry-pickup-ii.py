class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        dp=[[[-1]*c for _ in range(c)]for _ in range(r)]
        def fun(i,j,x,y,grid,r,c):
            if j==y:
                return 0
           # print("hi")
            if i<0 or j<0 or i>=r or j>=c:
                return 0
            if x<0 or y<0 or x>=r or y>=c:
                return 0
            if dp[i][j][y]!=-1:
                return dp[i][j][y]
            ans=-9999999999999
            ans=max(ans,fun(i+1,j+1,x+1,y+1,grid,r,c)+grid[i][j]+grid[x][y])
            ans=max(ans,fun(i+1,j+1,x+1,y,grid,r,c)+grid[i][j]+grid[x][y])
            ans=max(ans,fun(i+1,j+1,x+1,y-1,grid,r,c)+grid[i][j]+grid[x][y])
            ans=max(ans,fun(i+1,j,x+1,y+1,grid,r,c)+grid[i][j]+grid[x][y])
            ans=max(ans,fun(i+1,j,x+1,y,grid,r,c)+grid[i][j]+grid[x][y])
            ans=max(ans,fun(i+1,j,x+1,y-1,grid,r,c)+grid[i][j]+grid[x][y])
            ans=max(ans,fun(i+1,j-1,x+1,y+1,grid,r,c)+grid[i][j]+grid[x][y])
            ans=max(ans,fun(i+1,j-1,x+1,y,grid,r,c)+grid[i][j]+grid[x][y])
            ans=max(ans,fun(i+1,j-1,x+1,y-1,grid,r,c)+grid[i][j]+grid[x][y])
            dp[i][j][y]=ans
            return dp[i][j][y]
        return fun(0,0,0,c-1,grid,r,c)
        