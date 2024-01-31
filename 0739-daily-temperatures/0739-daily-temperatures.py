class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        l=[0]*len(temp)
        st=[]
        for i in range(len(temp)-1,-1,-1):
            while(len(st)>0 and temp[st[-1]]<=temp[i]):
                st.pop()
            if len(st)>0:
                l[i]=st[-1]-i
            st.append(i)
            
        return l
                    
        