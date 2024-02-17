class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders)
    {
        int n=heights.size();
        priority_queue<int>l;
        for(int i=0;i<n-1;i++)
        {
            int diff=heights[i+1]-heights[i];
            if (diff>0)
            {
                l.push(-1*diff);
            }
            if(l.size()>ladders)
            {
                bricks+=l.top();
                l.pop();
            }
            if(bricks<0)
            {
                return i;
            }
        }
        return n-1;
    }
};