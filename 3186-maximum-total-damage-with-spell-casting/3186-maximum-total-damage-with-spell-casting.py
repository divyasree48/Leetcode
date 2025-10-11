class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        @cache
        def fun(ind):
            if ind >= n:
                return 0
            skip = fun(ind + c[s[ind]])
            cur = s[ind] * c[s[ind]]
            take = cur + fun(ind2[ind])
            return max(skip, take)

        n = len(power)
        c = Counter(power)
        s = sorted(power)

        ind2 = [0] * n
        i = 0
        while i < n:
            val = s[i]
            ind2[i] = bisect_right(s, val + 2, i + 1)
            i += 1

        return fun(0)
        