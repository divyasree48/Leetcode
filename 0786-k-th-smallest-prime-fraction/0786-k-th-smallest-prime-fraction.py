class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l=[]
        n=len(arr)
        for i in range(n):
            for j in range(i+1,n):
                l.append([arr[i]/arr[j],arr[i],arr[j]])
        #print(l)
        l.sort()
        #print(l)
        ans=[]
        ans.append(l[k-1][1])
        ans.append(l[k-1][2])
        return ans
        