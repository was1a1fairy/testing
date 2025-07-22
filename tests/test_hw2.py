from hw2 import Vector
import pytest

@pytest.fixture()
def vec1():
    return Vector(2,3,5)

@pytest.fixture()
def vec2():
    return Vector(1, -2, 4)

def test_random_vector(vec1):
    assert vec1.random_vector()#what how

def test_lenth(vec1):
    assert vec1.lenth() == 38**0.5

def test_scalar_mul(vec1, vec2):
    assert vec1.scalar_mul(vec2) == 16

def test_angle_between(vec1, vec2):
    assert vec1.angle_between(vec2) == 16 / ((38 ** 0.5) * (21 ** 0.5))

def test_add(vec1, vec2):
    assert vec1.add(vec2).get_x() == 3
    assert vec1.add(vec2).get_y() == 1
    assert vec1.add(vec2).get_z() == 9