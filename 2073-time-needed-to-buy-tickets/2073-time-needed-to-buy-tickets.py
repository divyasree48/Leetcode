class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c=0
        i=0
        while(tickets[k]>0):
            if i>=len(tickets):
                i=0
            if tickets[i]>0:
                tickets[i]-=1
                c+=1
            i+=1
        return c
                
        
        