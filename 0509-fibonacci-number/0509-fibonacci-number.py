class Solution:
    def fib(self, n: int) -> int:
        def fun(n):
            if n<2:
                return n
            return fun(n-1)+fun(n-2)
        return fun(n)
