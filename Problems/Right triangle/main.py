class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here

    def is_right(self):
        return self.c ** 2 == self.a ** 2 + self.b ** 2

    def get_area(self):
        return self.a * self.b / 2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

triangle = RightTriangle(input_c, input_a, input_b)
print(triangle.get_area() if triangle.is_right() else 'Not right')
