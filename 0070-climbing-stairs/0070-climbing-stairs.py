class Solution:
    def climbStairs(self, n: int) -> int:
        a=b=1
        if n==1:
            return 1
        n-=1
        while(n):
            c=a+b
            a=b
            b=c
            n-=1
        return c
            
        