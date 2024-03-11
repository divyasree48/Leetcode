class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=''
        for i in order:
            for j in s:
                if j==i:
                    ans+=j
        for i in s:
            if i not in order:
                ans+=i
        return ans
        