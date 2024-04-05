class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for i in s:
            if st and ((ord(st[-1])+32) == ord(i) or (ord(st[-1])-32) == ord(i)):
                st.pop()
            else:
                st.append(i)
        return ''.join(st)