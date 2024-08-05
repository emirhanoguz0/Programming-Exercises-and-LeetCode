import math

class Circle:
    def __init__(self,r):
        self.radius = r
        self.pi = math.pi

    def area(self):
        return 4 * self.pi * self.radius