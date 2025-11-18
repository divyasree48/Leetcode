class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0
        ans = -1
        while i < n:
            if bits[i] == 1:
                i += 2
                ans = 2
            else: 
                i += 1
                ans = 1
        return ans == 1


        