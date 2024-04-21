class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[]for i in range(n)]
        for i in edges:
            a=i[0]
            b=i[1]
            adj[a].append(b)
            adj[b].append(a)
        vis=[0]*n
        def dfs(vis,source):
            vis[source]=1
            for i in adj[source]:
                if vis[i]==0:
                    dfs(vis,i)
        dfs(vis,source)
        if vis[destination]:
            return 1
        return 0
            