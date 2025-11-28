class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        def dfs(node,par):
            s = values[node]
            for neig in adj[node]:
                if neig != par:
                    s += dfs(neig,node)
            if s % k == 0:
                nonlocal c
                c += 1
            return s
        adj = [[] for i in range(n)]
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        c = 0
        dfs(0,-1)
        return c
        