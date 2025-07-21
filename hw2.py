from __future__ import annotations
import random
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

    def sub(self, other: Vector):
        return Vector(self.__x - other.get_x, self.__y - other.get_y, self.__z - other.get_z)

    def scalar_mul(self, other: Vector):
        return self.__x * other.get_x() + self.__y * other.get_y() + self.__z * other.get_z()

    def angle_between(self, other: Vector):
        return (self.scalar_mul(other))/(((self.__z**2 + self.__y**2 + self.__x**2)**0.5) * (other.get_y()**2 + other.get_x()**2 + other.get_z()**2)**0.5)

    def random_vector(self):
        return Vector(random.randint(1,10), random.randint(1,10), random.randint(1,10))

    def __str__(self):
        return f"Vector: {self.__x}, {self.__y}, {self.__z}."