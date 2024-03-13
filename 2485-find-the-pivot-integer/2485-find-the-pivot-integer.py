class Solution:
    def pivotInteger(self, n: int) -> int:
        summ=(n*(n+1))//2
        c=0
        for i in range(1,n+1):
            c+=i
            #print(c,summ-c+i)
            if c==summ-c+i:
                return i
            
        return -1
        
        