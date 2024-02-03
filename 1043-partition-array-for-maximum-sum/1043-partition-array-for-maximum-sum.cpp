class Solution {
public:
    int fun(int ind,int n,vector<int>&arr,int k,vector<int>&dp)
    {
        
        if(ind==n)return 0;
        if(dp[ind]!=-1)return dp[ind];
        int cs=0,cm=0;
        for(int j=ind;j<min(ind+k,n);j++)
        {
            cm=max(cm,arr[j]);
            int p=cm*(j-ind+1)+fun(j+1,n,arr,k,dp);
            cs=max(cs,p);
        }
        return dp[ind]=cs;

    }
    int maxSumAfterPartitioning(vector<int>& arr,int k) {
        int n=arr.size();
        vector<int>dp(n+1,-1);
        return fun(0,n,arr,k,dp);
    }
};