class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        par={}
        def findd(x):
            if par[x]==x:
                return x
            else:
                par[x]=findd(par[x])
                return par[x]
        def unionn(a,b):
            x=findd(a)
            y=findd(b)
            par[y]=x
        for i,j,k,l in equations:
            if i not in par.keys():
                par[i]=i
            if l not in par.keys():
                par[l]=l
            if j=="=":
                unionn(i,l)
        for i,j,k,l in equations:
            if j=="=":
                if findd(i)!=findd(l):
                    return 0
            else:
                if findd(i)==findd(l):
                    return 0
        return 1
                    
        