class Solution {
public:
    int maximumEnergy(vector<int>& e, int k) {
        int n=e.size();
        int ans=INT_MIN;
        for(int i=n-1;i>=n-k;i--)
        {
            int c=0;
            for(int j=i;j>=0;j=j-k)
            {
                c+=e[j];
                ans=max(ans,c);
            }
        }
        return ans;
        
    }
};