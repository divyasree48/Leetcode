class Solution {
public:
    long long dp[1001][1001];
    int mod=1e9+7;
    long long fun(int n,int k)
    {
        if(k==0)return 1;
        if(k<0 or n<0)return 0;
        if(dp[n][k]!=-1)return dp[n][k];
        long long ans=0;
        for(int i=0;i<n;i++)
        {
            if (k-i>=0)
                ans+=fun(n-1,k-i)%mod;
        }
        return dp[n][k]=ans%mod;
        
        
    }
    int kInversePairs(int n, int k) {
        memset(dp,-1,sizeof(dp));
        return fun(n,k)%mod;
        
    }
};