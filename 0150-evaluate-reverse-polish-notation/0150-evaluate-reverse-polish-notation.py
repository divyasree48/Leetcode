class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
            
        s="+-*/"
        l=[]
        for i in tokens:
            #print(l)
            if i[0] in s:
                if len(i)==1:
                    a=int(l[-1])
                    l.pop()
                    b=int(l[-1])
                    l.pop()
                    if i=='*':
                        l.append(str(a*b))
                    if i=='/':
                        l.append(str(int(b/a)))
                    if i=='+':
                        l.append(str(a+b))
                    if i=='-':
                        l.append(str(b-a))
                else:
                    l.append(i)
            else:
                l.append(i)
            #print(6//(-132))
        return int(l[-1])
        