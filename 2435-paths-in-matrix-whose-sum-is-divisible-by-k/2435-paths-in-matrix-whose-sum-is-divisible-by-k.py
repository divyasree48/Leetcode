class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        mod = 1000000007
        m = len(grid)
        n = len(grid[0])
        @cache
        def fun(i,j,s):
            if i == m or j == n:
                return 0
            if i == m-1 and j == n-1:
                if (s + grid[i][j])%k == 0:
                    return 1
                else:
                    return 0
            c = (s+grid[i][j]) % k
            return (fun(i+1,j,c) + fun(i,j+1,c)) % mod
        ans = fun(0,0,0)
        fun.cache_clear()
        return ans
        