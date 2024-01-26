class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, row: int, col: int) -> int:
        mod=1000000007
        dp=[[[-1 for i in range(maxMove+1)]for j in range(n+1)]for _ in range(m+1)]
        def fun(i,j,m,n,k):
            if k<0:
                return 0
            if i<0 or i>=m or j<0 or j>=n:
                return 1
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            
            dp[i+1][j][k-1]=fun(i+1,j,m,n,k-1)
            a=dp[i+1][j][k-1]



            dp[i-1][j][k-1]=fun(i-1,j,m,n,k-1)
            b=dp[i-1][j][k-1]



            dp[i][j+1][k-1]=fun(i,j+1,m,n,k-1)
            c=dp[i][j+1][k-1]



            dp[i][j-1][k-1]=fun(i,j-1,m,n,k-1)
            d=dp[i][j-1][k-1]
                
            dp[i][j][k]=sum([a,b,c,d])  
            return dp[i][j][k]%mod
        return fun(row,col,m,n,maxMove)%mod
        