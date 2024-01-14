class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        a=len(word1)
        b=len(word2)
        if a!=b:
            return 0
        if list(set(sorted(word1)))!=list(set(sorted(word2))):
            return 0
        d={}
        l=[]
        m=[]
        for i in word1:
            if i in d.keys():
                d[i]+=1
                l.append(d[i])
            else:
                d[i]=1
                l.append(d[i])
        d1={}
        for i in word2:
            if i in d1.keys():
                
                d1[i]+=1
                m.append(d1[i])
            else:
                
                d1[i]=1
                m.append(d1[i])
                         
        if sorted(l)==sorted(m):
            return 1
        return 0
        
        
        
                