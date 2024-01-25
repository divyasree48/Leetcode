class Solution {
public:
    void merge(vector<int>& nums,int low,int mid,int high,int &c)
    {
        int a[high+1];
        int i=low,j=mid+1,k=low;
        while(i<=mid and j<=high)
        {
            if(2LL*nums[j]>=nums[i]){
                c+=j-mid-1;
                    i++;
            }
            else j++;
        }
        if(i<=mid)
            c+=(mid-i+1)*(j-mid-1);
        i=low;
        j=mid+1;
        while(i<=mid and j<=high)
        {
            if(nums[i]<=nums[j])
                a[k++]=nums[i++];
            else
                a[k++]=nums[j++];
        }
        while(i<=mid)
            a[k++]=nums[i++];
        while(j<=high)
            a[k++]=nums[j++];
        for(int i=low;i<=high;i++)
            nums[i]=a[i];
    }
    void mergesort(vector<int>&nums,int low,int high,int &c)
    {
        if(low>=high)return;
        int mid=low+(high-low)/2;
        mergesort(nums,low,mid,c);
        mergesort(nums,mid+1,high,c);
        merge(nums,low,mid,high,c);
    }
    int reversePairs(vector<int>& nums) 
    {
        int c=0;
        mergesort(nums,0,nums.size()-1,c);
        return c;
    }
};