class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        l=sorted(d.items(),key=lambda x:x[1])[::-1]
        #print(l)
        ans=''
        for i,j in l:
            x=j
            while(x):
                ans+=i
                x-=1
        return ans
        