from hw2 import Vector
import pytest

@pytest.fixture()
def vector():
    return Vector.random_vector()

