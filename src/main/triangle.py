from itertools import permutations


class Triangle(object):
    def __init__(self, side1, side2, side3):

        if any([side1, side2, side3]) <= 0:
            raise ValueError("The length of a Triangle's side must be a positive int")

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

    @property
    def is_equilateral(self):
        return self.side1 == self.side2 == self.side3

    @property
    def is_right(self):
        # Find index of longest side and pop it into c,
        # sides is a read only property, so make a copy to pop/unpack correctly
        sides = self.sides
        max_index = sides.index(max(sides))
        c = sides.pop(max_index)
        a,b = sides
        return a ** 2 + b ** 2 == c ** 2

    def is_valid_triangle(self):
        # Triangle inequality, sum of any two sides  must be > third
        # Check each side against all the others. Note that a combination is not the same as a unique permutation
        # e.g, the combination a = 2, b = 3, c = 5 is incorrect, where permutations include a = 5, b = 3, c = 2
        # limit calculations to unique permutations only to avoid repeating 3,3,3 and 3,3,3
        sides = self.sides
        for p in set(permutations(sides, len(sides))):
            a,b,c = p
            if a >= (b + c):
                return False
        return True

    @property
    def is_isosceles(self):
        return bool([s for s in self.sides if self.sides.count(s) == 2 ])

    @property
    def is_scalene(self):
        return self.is_valid_triangle() and not (self.is_equilateral or self.is_isosceles or self.is_right)

