class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int k=nums.size();
        int s=(k*(k+1))/2;
        int c=0;
        for(auto it:nums) c+=it;
        return s-c;
    }
};