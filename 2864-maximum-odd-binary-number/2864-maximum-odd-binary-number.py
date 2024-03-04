class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a=s.count('1')
        b=s.count('0')
        s1=''
        for i in range(a-1):
            s1+='1'
        for i in range(b):
            s1+='0'
        s1+='1'
        return s1
        