class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        arr.sort()
        cnt=0
        for i in arr:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
                cnt+=1
        l=dict(sorted(d.items(),key=lambda x:x[1]))
        
        for i in l.keys():
            if k-l[i]<0:
                return cnt
            k-=l[i]
            cnt-=1
        return cnt