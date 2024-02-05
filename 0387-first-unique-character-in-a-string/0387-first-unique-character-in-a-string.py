class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=defaultdict(list)
        for i in range(len(s)):
            d[s[i]].append(i)
        for i in d.keys():
            a=d[i]
            if len(a)==1:
                return a[0]
        return -1
                
        