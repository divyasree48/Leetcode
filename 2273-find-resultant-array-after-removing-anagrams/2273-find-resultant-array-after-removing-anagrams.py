class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        l=[]
        for i in range(1,len(words)):
            if sorted(words[i])==sorted(words[i-1]):
                l.append(i)
        ans=[]
        for i in range(len(words)):
            if i not in l:
                ans.append(words[i])
        return ans