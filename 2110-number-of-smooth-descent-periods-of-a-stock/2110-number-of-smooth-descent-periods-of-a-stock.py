class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 1
        k = 1
        for i in range(1,len(prices)):
            if prices[i] == prices[i-1] - 1:
                k += 1
            else:
                k = 1
            ans += k
        return ans
        