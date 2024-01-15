class Solution:
    def findWinners(self, m: List[List[int]]) -> List[List[int]]:
        d={}
        
        l=[[]for i in range(2)]
        for i in m:
            if i[0] not in d.keys():
                d[i[0]]=0
            if i[1] in d.keys():
                d[i[1]]+=1
            else:
                d[i[1]]=1
        
        for i in d.keys():
            if d[i]==0:
                l[0].append(i)
                
            if d[i]==1:
                l[1].append(i)
                
        l[0].sort()
        l[1].sort()
        return l
                
        