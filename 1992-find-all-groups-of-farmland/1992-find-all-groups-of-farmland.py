class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        r=len(land)
        c=len(land[0])
        ans=[]
        vis=[[1 for i in range(c+10)]for j in range(r+10)]
        def dfs(m,n,a,b):
            if m<0 or m>=r or n<0 or n>=c or land[m][n]==0:
                return
            vis[m][n]=0
            land[m][n]=0
            if m>a[0] or n>b[0]:
                a[0]=m
                b[0]=n
            if vis[m-1][n]:
                dfs(m-1,n,a,b)
            if vis[m][n-1]:
                dfs(m,n-1,a,b)
            if vis[m+1][n]:
                dfs(m+1,n,a,b)
            if vis[m][n+1]:
                dfs(m,n+1,a,b)
        for i in range(r):
            for j in range(c):
                if land[i][j]==1:
                    l=[]
                    a=[-1]
                    b=[-1]
                    dfs(i,j,a,b)
                    print(i,j,a,b)
                    a=a[0]
                    b=b[0]
                    if a==-1 or b==-1:
                        continue
                    if i<a:
                        l.append(i)
                        l.append(j)
                        l.append(a)
                        l.append(b)
                    elif i==a:
                        if j<b:
                            l.append(i)
                            l.append(j)
                            l.append(a)
                            l.append(b)
                        else:
                            l.append(a)
                            l.append(b)
                            l.append(i)
                            l.append(j)
                    else:
                            l.append(a)
                            l.append(b)
                            l.append(i)
                            l.append(j)
                    ans.append(l)
        return ans
                        
                    