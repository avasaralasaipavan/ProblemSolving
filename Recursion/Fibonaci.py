class Solution:

    def __init__(self):
        self.dit = {1:1,0:0}
    def fib(self, n: int) -> int:

        if n in self.dit:
            return self.dit[n]

        data = self.fib(n-2)+self.fib(n-1)
        self.dit[n] = data
        return data
        

s = Solution()
print(s.fib(10))
print(s.dit)