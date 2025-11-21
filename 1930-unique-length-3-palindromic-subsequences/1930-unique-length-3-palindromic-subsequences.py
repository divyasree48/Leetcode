class Solution:
    
    def countPalindromicSubsequence(self, s: str) -> int:
        leftset = [-1] * 26
        n = len(s)
        for i in range(n):
            ind = ord(s[i]) - ord('a')
            if leftset[ind] == -1:
                leftset[ind] = i # left most index of a character
        rightmost = [0] * 26
        inbtwn = [set() for i in range(26)]
        ans = 0
        for i in range(n-1, -1, -1):
            ind = ord(s[i]) - ord('a')
            if leftset[ind] == i:
                ans += len(inbtwn[ind])
            for j in range(26):
                if rightmost[j]:
                    inbtwn[j].add(s[i])
            if rightmost[ind] == 0:
                rightmost[ind] = 1
        return ans

        