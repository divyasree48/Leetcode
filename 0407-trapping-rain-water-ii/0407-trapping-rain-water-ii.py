class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        vis = [[False] * cols for i in range(rows)]
        min_heap = []
        for i in range(rows):
            for j in range(cols):
                if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                    heappush(min_heap, (heightMap[i][j], i, j))
                    vis[i][j] = True
        c = 0
        dir = ((-1, 0), (0, 1), (1, 0), (0, -1))
        while min_heap:
            height, x, y = heappop(min_heap)
            for a, b in dir:
                p, q = x + a, y + b
                if 0 <= p < rows and 0 <= q < cols and not vis[p][q]:
                    c += max(0, height - heightMap[p][q])
                    vis[p][q] = True
                    heappush(min_heap, (max(height, heightMap[p][q]), p, q))
        return c

        