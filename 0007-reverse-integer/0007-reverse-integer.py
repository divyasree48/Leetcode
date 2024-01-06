class Solution:
    def reverse(self, x: int) -> int:
        
        if x<0:
            p=1
            x=x*-1
        else:
            p=0
        
        if x%10==0:
            x=x//10
        s=str(x)
        s1=s[::-1]
        if p==1:
            s1='-'+s1
        if int(s1)<-2147483648 or int(s1)>2147483647:
            return 0
        else:
            return int(s1)
        