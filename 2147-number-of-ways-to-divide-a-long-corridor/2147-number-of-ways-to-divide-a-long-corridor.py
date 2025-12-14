class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 1000000007
        @cache
        def fun(ind,seats):
            if ind >= len(corridor):
                if seats == 2:
                    return 1
                return 0
            if corridor[ind] == "S":
                seats += 1
            if seats > 2:
                return 0
            c = fun(ind+1, seats)
            if seats == 2:
                c = (c + fun(ind+1, 0))%mod
            return c
        res = fun(0,0)
        fun.cache_clear()
        return res
        