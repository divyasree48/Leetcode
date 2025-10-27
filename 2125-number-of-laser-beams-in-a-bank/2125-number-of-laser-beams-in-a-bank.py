class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l = []
        for i in bank:
            s = i.count('1')
            if s > 0:
                l.append(s)
        n = len(l)
        ans = 0
        for i in range(1,n):
            ans += l[i] * l[i-1]
        return ans
        