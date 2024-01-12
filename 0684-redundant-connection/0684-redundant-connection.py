class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par=[i for i in range(1+len(edges))]
        def found(x):
            if par[x]==x:
                return x
            else:
                par[x]=found(par[x])
                return par[x]
        def unionn(a,b):
            x=found(a)
            y=found(b)
            par[y]=x
        p=q=0
        
        for i,j in edges:
            if found(i)==found(j):
                p=i
                q=j
            else:
                unionn(i,j)
        return [p,q]
        
        
        