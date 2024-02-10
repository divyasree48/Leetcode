class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        l=[]
        for i in range(n):
            l.append(s[i])
            a=s[i]
            for j in range(i+1,n):
                a+=s[j]
                if a==a[::-1]:
                    l.append(a)
        return len(l)
        