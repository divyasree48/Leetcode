class Solution:
    def sumOfMultiples(self, n: int) -> int:
        c=0
        for i in range(3,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                c+=i
        return c
        