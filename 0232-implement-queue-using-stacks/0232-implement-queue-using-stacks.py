class MyQueue:

    def __init__(self):
        self.l=[]

    def push(self, x: int) -> None:
        self.l.append(x)

    def pop(self) -> int:
        x=self.l[0]
        self.l.pop(0)
        return x

    def peek(self) -> int:
        return self.l[0]

    def empty(self) -> bool:
        if len(self.l)==0:
            return 1
        return 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()