class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*501 for i in range(501)]
        def fun(i,j,n,m,a,b):
            if i>=n or j>=m:
                return max(n-i,m-j)
            if dp[i][j]!=-1:
                return dp[i][j]
            if a[i]==b[j]:
                return fun(i+1,j+1,n,m,a,b)
            else:
                x=1+fun(i,j+1,n,m,a,b)
                y=1+fun(i+1,j,n,m,a,b)
                z=1+fun(i+1,j+1,n,m,a,b)
                dp[i][j]=min(x,y,z)
                return min(x,y,z)
        return fun(0,0,len(word1),len(word2),word1,word2)
        