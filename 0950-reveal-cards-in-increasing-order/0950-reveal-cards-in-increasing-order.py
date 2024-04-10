class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        l=sorted(deck)[::-1]
        n=len(deck)
        q=[]
        ans=[]
        #print(l)
        q.append(l[0])
        for i in range(1,n):
            q.insert(0,q[-1])
            q.pop()
            q.insert(0,l[i])
            #print(q)
        return q
        