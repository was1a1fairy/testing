from __future__ import annotations
import random
import math

class Vector:


    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z


    def __check_other(self, x, y, z):
        if not isinstance(x, int): raise TypeError
        if not isinstance(y, int): raise TypeError
        if not isinstance(z, int): raise TypeError


    def get_x(self):
        return int(self.__x)

    def get_y(self):
        return int(self.__y)

    def get_z(self):
        return int(self.__z)


    def length(self):
        return ((self.__x**2)+(self.__y**2)+(self.__z**2))**0.5


    def add(self, other: Vector):
        self.__check_other(other.__x, other.__y, other.__z)
        return Vector(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)


    def sub(self, other: Vector):
        self.__check_other(other.__x, other.__y, other.__z)
        return Vector(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)


    def scalar_mul(self, other: Vector):
        self.__check_other(other.__x, other.__y, other.__z)
        return self.__x * other.get_x() + self.__y * other.get_y() + self.__z * other.get_z()


    def angle_between(self, other: Vector):

        self.__check_other(other.__x, other.__y, other.__z)

        if self.__x == self.__y == self.__z:
            raise ValueError("нельзя найти угол между вектором и точкой((")
        if other.__z == other.__y == other.__x:
            raise ValueError("нельзя найти угол между вектором и точкой((")

        return math.acos(self.scalar_mul(other)/(self.length()*other.length()))


    def random_vector(self):
        return Vector(random.randint(1,10), random.randint(1,10), random.randint(1,10))

class Circle:

    def __init__(self, r: int):
        self.__r = r

    def area(self):
        return math.pi * self.__r**2

    def circumference(self):
        return 2 * math.pi * self.__r

    def diameter(self):
        return 2 * self.__r