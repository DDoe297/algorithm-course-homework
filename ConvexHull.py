from functools import total_ordering
from math import sqrt


@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.y < other.y if self.x == other.x else self.x < other.x

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'({self.x},{self.y})'

class Line:
    def __init__(self, point_one, point_two):
        self.point_one = point_one
        self.point_two = point_two

    def __eq__(self, other):
        return self.point_one == other.point_one and self.point_two == other.point_two

    def is_point_right_of_line(self, point):
        return ((self.point_two.x - self.point_one.x)*(point.y - self.point_one.y) - (self.point_two.y - self.point_one.y)*(point.x - self.point_one.x)) < 0

    def distance(self, point):
        return abs((self.point_two.x-self.point_one.x)*(self.point_one.y-point.y)-(self.point_one.x-point.x)*(self.point_two.y-self.point_one.y))/sqrt((self.point_two.x-self.point_one.x)**2+(self.point_two.y-self.point_one.y)**2)

    def __str__(self):
        return f'{self.point_one} - {self.point_two}'

    def __repr__(self):
        return f'{self.point_one} - {self.point_two}'

    def __hash__(self):
        return hash(str(self))


def convex_hull(points):
    points.sort()
    A = points[0]
    B = points[-1]
    AB = Line(A, B)
    BA = Line(B, A)
    x0 = [point for point in points if AB.is_point_right_of_line(point)]
    x1 = [point for point in points if BA.is_point_right_of_line(point)]
    solution = {AB, BA}
    solution = find_hull(x0, AB, solution)
    solution = find_hull(x1, BA, solution)
    return solution


def find_hull(points, line, solution):
    if not points:
        return solution
    else:
        C = max(points, key=line.distance)
        AC = Line(line.point_one, C)
        CB = Line(C, line.point_two)
        solution = (solution-{line}).union({AC, CB})
        x0 = [point for point in points if AC.is_point_right_of_line(point)]
        x1 = [point for point in points if CB.is_point_right_of_line(point)]
        solution = find_hull(x0, AC, solution)
        solution = find_hull(x1, CB, solution)
        return solution


points = []
points.append(Point(5, -3))
points.append(Point(-3, 2))
points.append(Point(-6, -4))
points.append(Point(0, -5))
points.append(Point(1, 7))
points.append(Point(2, 2))
points.append(Point(3, 4))
points.append(Point(1, 1))
points.append(Point(4, 0))
for line in convex_hull(points):
    print(line)
