'''

Scenario
Now we're going to embed the Point class (see Lab 3.4.1.14) inside another class. Also, we're going to put three points into one class, which will let us define a triangle. How can we do it?

The new class will be called Triangle and this is the list of our expectations:
    the constructor accepts three arguments - all of them are objects of the Point class;
    the points are stored inside the object as a private list;
    the class provides a parameterless method called perimeter(), which calculates the perimeter of the triangle described by the three points; the perimeter is a sum of all legs' lengths (we mention it for the record, although we are sure that you know it perfectly yourself.)

Complete the template we've provided in the editor. Run your code and check whether the evaluated perimeter is the same as ours.

Expected output
    3.414213562373095

'''

from math import hypot


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return hypot(x, y) - hypot(self.__x, self.__y)

    def distance_from_point(self, point):
        return hypot(point.getx(), point.gety()) + hypot(self.__x, self.__y)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        # Private list with all the tringle points
        self.__tringle = [vertice1, vertice2, vertice3]

    # Method to get the perimeter of the tringle
    def perimeter(self):
        # Variable where the result is created
        result = 0.0

        result += self.__tringle[0].distance_from_point(self.__tringle[1])
        result += self.__tringle[1].distance_from_point(self.__tringle[2])
        result += self.__tringle[0].distance_from_point(self.__tringle[2])

        return result


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
