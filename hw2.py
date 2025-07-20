from __future__ import annotations
class Vector:

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def lenth(self):
        return 0.5**((self.__x**2)+(self.__y**2)+(self.__z**2))

    def add(self, other: Vector):
        return Vector(self.__x + other.get_x, self.__y + other.get_y, self.__z + other.get_z)