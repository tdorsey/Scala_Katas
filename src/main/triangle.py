class Triangle(object):
    def __init__(self, side1, side2, side3):
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3



    @property
    def sides(self):
        return [self.side1, self.side2, self.side3]

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, value):
        self._side1 = value

    @property
    def side2(self):
        return self._side2

    @side2.setter
    def side2(self, value):
        self._side2 = value

    @property
    def side3(self):
        return self._side3

    @side3.setter
    def side3(self, value):
        self._side3 = value

    def is_equilateral(self):
        return self.side1 == self.side2 == self.side3

    def is_right(self):
        return True

    def is_isosceles(self):
        return bool([side for side in self.sides if self.sides.count(side) == 2])
    def is_scalene(self):
        return True
