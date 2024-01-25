class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1]*(len(text2)+1)for i in range(len(text1)+1)]
        def fun(a,b,i,j,n,m):
            if i>=n or j>=m:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if a[i]==b[j]:
                dp[i][j]=fun(a,b,i+1,j+1,n,m)+1
                return dp[i][j]
            dp[i][j]=max(fun(a,b,i+1,j,n,m),fun(a,b,i,j+1,n,m))
            return dp[i][j]
        return fun(text1,text2,0,0,len(text1),len(text2))
        