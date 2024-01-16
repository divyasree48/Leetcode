class RandomizedSet:

    def __init__(self):
        self.s=set()
        

    def insert(self, val: int) -> bool:
        s=self.s
        if val not in s:
            s.add(val)
            return 1
        return 0

    def remove(self, val: int) -> bool:
        s=self.s
        if val in s:
            s.remove(val)
            return 1
        return 0
        

    def getRandom(self) -> int:
        s=self.s
        return random.choice(list(s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()