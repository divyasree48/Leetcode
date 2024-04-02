class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d=defaultdict(list)
        for i in range(len(t)):
            a=t[i]
            d[a].append(i)
        d1=defaultdict(list)
        for i in range(len(s)):
            a=s[i]
            d1[a].append(i)
        for i in d.values():
            if i not in d1.values():
                return 0
        return 1
        