class Solution:
    def maxOperations(self, s: str) -> int:
        res = 0
        c = 0
        for i in range(len(s)):
            char = s[i]
            if char == '1':
                c += 1
            elif i > 0 and s[i-1] == '1':
                res += c
        return res


        
        