class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        mp={}
        for i in roads:
            for j in i:
                if j in mp.keys():
                    mp[j]+=1
                else:
                    mp[j]=1
        smp={j:i for j,i in sorted(mp.items(),key=lambda item:item[1],reverse=True)}
        #print(smp)
        k=n
        for i in smp.keys():
            smp[i]=k
            k-=1
        #print(smp)
        ans=0
        for i in roads:
            ans+=smp[i[0]]+smp[i[1]]
        return ans
        
        
        