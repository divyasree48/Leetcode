class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        dp = set()
        def dfs(s):
            if s in dp:
                return
            dp.add(s)
            s1 = []
            for i in range(n):
                if i & 1:
                    ele = int(s[i]) + a
                    ele = ele % 10
                    s1.append(str(ele))
                else:
                    s1.append(s[i])
            s1 = ''.join(s1)
            s2 = s[n-b::] + s[:n-b:]
            dfs(s1)
            dfs(s2)
        dfs(s)
        #print(dp)
        return min(dp)

        