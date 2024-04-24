class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        l=[0,1,1]
        while(n-2):
            l.append(l[-1]+l[-2]+l[-3])
            n-=1
        return l[-1]
        