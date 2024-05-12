class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans=[]
        r=len(grid)
        c=len(grid[0])
        for i in range(r-2):
            li=[]
            for j in range(c-2):
                maxi=0
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        maxi=max(maxi,grid[k][l])
                li.append(maxi)
            ans.append(li)
        return ans
                
                        