class Solution:
    def maxDepth(self, s: str) -> int:
        st=[]
        maxi=0
        for i in s:
            if i=='(':
                st.append('(')
            if i==')':
                st.pop()
            maxi=max(maxi,len(st))
        return maxi