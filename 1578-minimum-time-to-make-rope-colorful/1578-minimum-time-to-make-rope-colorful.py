class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        cur = 0
        n = len(colors)
        while cur < n:
            start = cur
            s = 0
            maxi = 0
            while cur < n and colors[cur] == colors[start]:
                s += neededTime[cur]
                if maxi < neededTime[cur]:
                    maxi = neededTime[cur]
                cur += 1
            if cur - start > 1:
                total += s - maxi
        return total

        