import math

class ESC_TreeNumber():
    def __init__(self, n):
        self.n = n
    
    def unrooted(self):
        try:
            return str(int(math.factorial(2 * self.n - 5) / ((2**(self.n-3)) * math.factorial(self.n - 3))))
        except ValueError:
            return "1"
    
    def rooted(self):
        try:
            return str(int(math.factorial(2 * self.n - 3) / ((2**(self.n-2)) * math.factorial(self.n - 2))))
        except ValueError:
            return "1"