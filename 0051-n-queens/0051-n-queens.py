class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        grid=[[0]*n for _ in range(n)]
        def valid(i,j,n,grid):
            x=i
            y=j
            while(x>=0):
                if grid[x][y]:
                    return 0
                x-=1
            x=i
            y=j
            while(x>=0 and y>=0):
                if grid[x][y]:
                    return 0
                x-=1
                y-=1
            x=i
            y=j
            while(x>=0 and y<n):
                if grid[x][y]:
                    return 0
                x-=1
                y+=1
            return 1
                
        def fun(i,n,grid):
            if i==n:
                v=[]
                for p in range(n):
                    s=''
                    for q in range(n):
                        if grid[p][q]==0:
                            s+='.'
                        else:
                            s+='Q'
                        #print(s)
                    v.append(s)
                    if p==n-1 and q==n-1:
                        #v.append(s)
                        #print(v,p,q)
                        ans.append(v)
                
                return
            for j in range(n):
                if valid(i,j,n,grid):
                    grid[i][j]=1
                    fun(i+1,n,grid)
                    grid[i][j]=0
        fun(0,n,grid)
        res=[]
        for i in ans:
            res.append("".join(i))
        return ans
        