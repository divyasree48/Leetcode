class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [[0]*n for i in range(n)]
        for r1,c1,r2,c2 in queries:
            mat[r1][c1] += 1
            if r2 + 1 < n:
                mat[r2+1][c1] -= 1
            if c2 + 1 < n:
                mat[r1][c2+1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                mat[r2+1][c2+1] += 1
        for r in range(n):
            for c in range(n):
                if r>0:
                    mat[r][c] += mat[r-1][c]
                if c>0:
                    mat[r][c] += mat[r][c-1]
                if r>0 and c>0:
                    mat[r][c] -= mat[r-1][c-1]
        return mat
                