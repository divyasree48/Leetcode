class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<0:
            return 0

        x=bin(n)[2::]
        if x.count('1')==1:
            return 1
        return 0


        
