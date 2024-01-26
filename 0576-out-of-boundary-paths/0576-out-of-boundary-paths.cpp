class Solution {
long long mod=1e9+7;
public:
    int boundary(vector<vector<vector<int>>> &dp,int i,int j,int m,int n,int k){
        if(k<0)
        return 0;
        if(i<0 or j<0 or i>=m or j>=n)
        return 1;
        int a,b,c,d;
        if(dp[i][j][k]!=-1)
        return dp[i][j][k]%mod;
        a=boundary(dp,i-1,j,m,n,k-1)%mod;
        b=boundary(dp,i,j-1,m,n,k-1)%mod;
        c=boundary(dp,i+1,j,m,n,k-1)%mod;
        d=boundary(dp,i,j+1,m,n,k-1)%mod;
        dp[i][j][k]=((a%mod+b%mod)%mod+(c%mod+d%mod)%mod)%mod;
        return dp[i][j][k]%mod;
    }
    int findPaths(int m, int n, int k, int startRow, int startColumn) {
        vector<vector<vector<int>>> dp(m+1,vector<vector<int>>(n+1,vector<int> (k+1,-1)));
        return boundary(dp,startRow,startColumn,m,n,k)%mod;
    }
};