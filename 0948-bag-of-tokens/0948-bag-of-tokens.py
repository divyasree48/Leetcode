class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        n=len(tokens)
        i=0
        j=n-1
        score=0
        while(i<=j):
            #print(power,score,tokens[i],tokens[j])
            
            if power>=tokens[i]:
                power-=tokens[i]
                score+=1
                i+=1
            elif score>0:
                if j-1<i:
                    break
                power+=tokens[j]
                score-=1
                j-=1
            else:
                break
        return score
        