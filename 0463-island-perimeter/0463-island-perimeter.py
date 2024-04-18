class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    if i-1<0:
                        c+=1
                    else:
                        if grid[i-1][j]==0:
                            c+=1
                    if i+1>=len(grid):
                        c+=1
                    else:
                        if grid[i+1][j]==0:
                            c+=1
                    if j-1<0:
                        c+=1
                    else:
                        if grid[i][j-1]==0:
                            c+=1
                    if j+1>=len(grid[0]):
                        c+=1
                    else:
                        if grid[i][j+1]==0:
                            c+=1
        return c
                    
                        
        