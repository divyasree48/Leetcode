class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        d={2:12,3:123,4:1234,5:12345,6:123456,7:1234567,8:12345678,9:123456789}
        size=int(log(low,10))+1
        maxi=int(log(high,10))+1
        ans=[]
        while(size<=maxi):
            a=d[size]
            for i in range(1,11-size):
                if a>=low and a<=high:
                    ans.append(a)
                a+=int('1'*size)
            size+=1
            if a>high:
                break
        return ans
                    
                
            
        