"""
Se Ho Lee
UPI: slee626
ID: 890218467
Question 2
"""

from FibonacciIterator import FibonacciIterator

class Fibonacci:

    def __init__(self, data,x=1,y=1):
        self.count = data
        self.x = x
        self.y = y

    def __iter__(self):
        return FibonacciIterator(self.count)
