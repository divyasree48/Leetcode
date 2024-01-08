class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        l=[{}for i in range(n)]
        cnt=0
        for i in range(1,n):
            for j in range(i):
                dif=nums[i]-nums[j]
                if dif in l[j].keys():
                    cnt+=l[j][dif]
                    if dif in l[i].keys():
                        l[i][dif]+=l[j][dif]+1
                    else:
                        l[i][dif]=l[j][dif]+1
                else:
                    
                    if dif in l[i].keys():
                        l[i][dif]+=1
                    else:
                        l[i][dif]=1
                    
        print(l)        
        return cnt