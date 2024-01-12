class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)//2
        c=0
        l="aeiouAEIOU"
        for i in range(n):
            if s[i] in l:
                c+=1
        for i in range(n,2*n):
            if s[i] in l:
                c-=1
        if c==0:
            return 1
        return 0
        