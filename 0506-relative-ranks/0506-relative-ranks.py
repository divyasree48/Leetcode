class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s=sorted(score)[::-1]
        n=len(score)
        for i in range(n):
            a=s.index(score[i])
            if a==0:
                score[i]="Gold Medal"
            elif a==1:
                score[i]="Silver Medal"
            elif a==2:
                score[i]="Bronze Medal"
            else:
                score[i]=str(a+1)
        return score
            
        