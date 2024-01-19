class Solution {
public:
    int fun(vector<vector<int>>& a,int i,int j,int n, vector<vector<int>>&dp)
    {
        if(i<0 || j<0 || i>n || j>=n) return 10000;
        if(i==n)
        {
            return 0;
        }
        if(dp[i][j]!=-10000) return dp[i][j];
        int l=a[i][j]+fun(a,i+1,j,n,dp);
        int r=a[i][j]+fun(a,i+1,j+1,n,dp);
        int d=a[i][j]+fun(a,i+1,j-1,n,dp);
        return dp[i][j]=min(l,min(r,d));
    }
    int minFallingPathSum(vector<vector<int>>& a) {
        int ans=INT_MAX,n=a.size();
        vector<vector<int>>dp(n+1,vector<int>(n+1,-10000));
        for(int i=0;i<n;i++)
        {
            ans=min(ans,fun(a,0,i,n,dp));
        }
        return ans;
    }
};