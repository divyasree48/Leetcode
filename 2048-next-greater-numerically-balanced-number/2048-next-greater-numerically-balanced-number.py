class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        i = n + 1
        while(1):
            l = [0] * 10
            ele = i
            while ele:
                r = ele % 10
                l[r] += 1
                ele = ele // 10
            f = 1
            for j in range(10):
                if l[j] == 0 or l[j] == j:
                    continue
                else:
                    f = 0
                    break
            if f:
                return i
            i += 1
            
        