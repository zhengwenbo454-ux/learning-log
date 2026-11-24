class Calculator:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def add(self, a, b):
        return a + b
    
    @classmethod
    def from_tuple(cls, t):
        return cls(*t)
    
    @staticmethod
    def is_positive(n):
        return n > 0

c1 = Calculator()
print(c1.add(1, 2))

c = Calculator.from_tuple((1,2))
print(c.add(1,2))

print(Calculator.is_positive(5))
print(Calculator.is_positive(-3))

