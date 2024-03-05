class Solution:
    def minimumLength(self, s: str) -> int:
        while(len(s)):
            if len(s)<2:
                break
            if s[0]==s[-1]:
                for i in range(len(s)):
                    if s[i]!=s[0]:
                        ind=i
                        break
                else:
                    ind=len(s)-1
                for i in range(len(s)-1,-1,-1):
                    if s[i]!=s[-1]:
                        indd=i
                        break
                else:
                    indd=0
                #print(s,ind,indd)
                
                if ind==len(s)-1:
                    s=''
                    break
                else:
                    s=s[ind:indd+1:]
            else:
                break
        return len(s)
                
                        
        