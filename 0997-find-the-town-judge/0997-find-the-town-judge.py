class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        summ=(n*(n+1))//2
        d=defaultdict(list)
        for i in range(1,n+1):
            d[i].append(0)
        c=0
        vis=[0]*(n+1)
        for i in trust:
            d[i[1]].append(i[0])
            if vis[i[0]]==0:
                vis[i[0]]=1
                c+=i[0]
        print(summ,c,d)
        if summ-c==0:
            return -1
        if len(d[summ-c])==n:
            return summ-c
        return -1
        