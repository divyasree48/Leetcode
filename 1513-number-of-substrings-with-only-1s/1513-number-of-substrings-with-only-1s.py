class Solution:
    def numSub(self, s: str) -> int:
        mod = 1000000007
        n = len(s)
        res = 0
        c = 1 if s[0] == '1' else 0
        for i in range(1,n):
            if s[i] == '1':
                c += 1
            else:
                res += (c*(c+1))//2
                c = 0
        res += (c*(c+1))//2
        return res % mod

        