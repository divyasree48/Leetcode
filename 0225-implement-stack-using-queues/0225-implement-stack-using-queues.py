class MyStack:

    def __init__(self):
        self.l=[]
        

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> int:
        x=self.l[-1]
        self.l.pop()
        return x
        

    def top(self) -> int:
        return self.l[-1]

    def empty(self) -> bool:
        if len(self.l)==0:
            return 1
        return 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()