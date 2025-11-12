class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def fun(n):
            res = 0
            c = 0
            k = 1
            while k <= n:
                l = k
                r = min(n, k * 4 - 1)
                c += 1
                res += (r - l + 1) * c
                k *= 4
            return res

        res = 0
        for l, r in queries:
            res += (fun(r) - fun(l - 1) + 1) // 2
        return res
        