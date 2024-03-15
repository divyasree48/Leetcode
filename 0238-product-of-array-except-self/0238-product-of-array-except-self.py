class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        c=0
        n=0
        for i in nums:
            n+=1
            if i==0:
                c+=1
            else:
                p*=i
        ans=[]
        if c==0:
            for i in nums:
                ans.append(p//i)
            return ans
        elif c==1:
            for i in nums:
                if i==0:
                    ans.append(p)
                else:
                    ans.append(0)
            return ans
        else:
            return [0]*n
            
        