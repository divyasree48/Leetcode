class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans=0
        p=n=0
        for i in operations:
            for j in i:
                if j=='-':
                    n+=1
                    break
                if j=='+':
                    p+=1
                    break
            if n==1:
                ans-=1
            if p==1:
                ans+=1
            n=0
            p=0
        return ans

