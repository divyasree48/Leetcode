class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        s=words[0]
        d={}
        for i in s:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in d.keys():
            l.append(d[i])
        n=len(words)
        for i in range(1,n):
            e={}
            st=words[i]
            for j in st:
                if j in e.keys():
                    e[j]+=1
                else:
                    e[j]=1
                    
            for k in s:
                if k in st:
                    a=min(e[k],d[k])
                    d[k]=a
                else:
                    d[k]=0
        ans=[]
        for i in d.keys():
            for j in range(d[i]):
                ans.append(i)
        return ans
                    