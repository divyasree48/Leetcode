class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if len(digits)==0:
            return []
        v=[]
        ans=[]
        def fun(ind,n,digits):
            if ind==n:
                a=v.copy()
                
                ans.append("".join(a))
                return
            for i in l[int(digits[ind])-2]:
                v.append(i)
                fun(ind+1,n,digits)
                v.pop()
        n=len(digits)
        fun(0,n,digits)
        return ans
        