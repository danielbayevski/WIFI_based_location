
from math import sqrt



class Point:

    def __init__(self, x = 0 , y =0):
        self.x = x or 0
        self.y = y or 0

    def toList(self, dimentions : int = 2) -> list[float]:
        return [self.x,self.y] if dimentions == 2 else [self.x,self.y,self.z]

    # def __repr__(self):
    #     rep = 'Point(' + self.x + ',' + self.y + ')'
    #     return rep

    def __str__(self):
        rep = 'Point(' + str(round(self.x, 2)) + ',' + str(round(self.y, 2)) + ')'
        return rep

    def distance(self, other):
        dist = (self.x - other.x)**2 +(self.y - other.y)**2
        return sqrt(dist)


