"""
Se Ho Lee
UPI: slee626
ID: 890218467
Question 2
"""

class FibonacciIterator:

    def __init__ (self, data):
        self.x = 1
        self.y = 1
        self.count = data

    def __next__(self):
        fibonacci = self.x
        if self.count <= 0:
            raise StopIteration
        else:
            self.count = self.count - 1
            self.x, self.y = self.y, (self.x + self.y)
            return fibonacci

    def __iter__(self):
        return self
