class Solution:
    def numSquares(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        def fun(n):
            if n==0:
                return 0
            if n<0:
                return 1000000000
            if dp[n]!=-1:
                return dp[n]
            ans=1000000000
            i=1
            while(i*i<=n):
                ans=min(ans,fun(n-(i*i))+1)
                i+=1
            dp[n]=ans
            return dp[n]
            
        
        return fun(n)
        