class Solution:
    def maxLength(self, arr: List[str]) -> int:
        l=[]
        ans=[]
        def fun(arr,n,i):
            if i==n:
                a=l.copy()
                b="".join(a)
                if len(b)==len(set(b)):
                    ans.append(b)
                return
            l.append(arr[i])
            fun(arr,n,i+1)
            l.pop()
            fun(arr,n,i+1)
        n=len(arr)
        fun(arr,n,0)
        return len(max(ans,key=len))
                    
        