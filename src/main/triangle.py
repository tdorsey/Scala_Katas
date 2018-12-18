class Triangle():

    @property
    def side1(self):
        return self._side1

    @side1.setter
    def side1(self, value):
        self._side1 = value

    @side1.getter
    def side1(self):
        return self._side1

    @property
    def side2(self):
        return self._side2

    @side1.setter
    def side2(self, value):
        self._side2 = value

    @side1.getter
    def side2(self):
        return self._side2

    @property
    def side3(self):
        return self._side3

    @side3.setter
    def side3(self, value):
        self._side3 = value

    @side3.getter
    def side3(self):
        return self._side3

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_equilateral(self):
        return True

    def is_right(self):
        return True

    def is_isosceles(self):
        return False
    def is_scalene(self):
        return False
