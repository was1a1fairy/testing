from hw2 import Vector
import pytest
import math

@pytest.fixture()
def vec_normal():
    return Vector(2,3,5)

@pytest.fixture()
def vec2_negative():
    return Vector(1, -2, 4)

@pytest.fixture()
def vec3_wrong():
    return Vector("мяу", 0, 0)

@pytest.fixture()
def vec4_o():
    return Vector(1, 2, 0)

@pytest.fixture()
def vec5_o():
    return Vector(2, -1, 10)

@pytest.fixture()
def vec6_k():
    return Vector(2,3,4)

@pytest.fixture()
def vec7_k():
    return Vector(6,9,12)

@pytest.fixture()
def vec8_zero():
    return Vector(0, 0, 0)



def test_length(vec_normal):
    assert vec_normal.length() == 38**0.5

def test_length_negative(vec2_negative):
    assert vec2_negative.length() == 21 ** 0.5

def test_length_zero(vec8_zero):
    assert vec8_zero.length() == 0



def test_scalar_mul(vec_normal, vec2_negative):
    assert vec_normal.scalar_mul(vec2_negative) == 16

def test_scalar_mul_wrong_type(vec_normal, vec3_wrong):
    with pytest.raises(TypeError):
        vec_normal.scalar_mul(vec3_wrong)

def test_scalar_mul_o(vec4_o, vec5_o):
    assert vec4_o.scalar_mul(vec5_o) == 0

def test_scalar_mul_k(vec6_k, vec7_k):
    assert vec6_k.scalar_mul(vec7_k) == 87

def test_scalar_mul_zero(vec_normal, vec8_zero):
    assert vec_normal.scalar_mul(vec8_zero) == 0



def test_angle_between(vec_normal, vec2_negative):
    assert vec_normal.angle_between(vec2_negative) == math.acos(16/(38**0.5*21**0.5))

def test_angle_between_wrong_type(vec_normal, vec3_wrong):
    with pytest.raises(TypeError):
        vec_normal.angle_between(vec3_wrong)

def test_angle_between_o(vec4_o, vec5_o):
    assert vec4_o.angle_between(vec5_o) == math.pi/2

def test_angle_between_k(vec6_k, vec7_k):
    assert vec6_k.angle_between(vec7_k) == 0
#     *грустный смайлик*

def test_angle_between_zero(vec_normal, vec8_zero):
    with pytest.raises(ValueError):
        vec_normal.angle_between(vec8_zero)


def test_add(vec_normal, vec2_negative):
    assert vec_normal.add(vec2_negative).get_x() == 3
    assert vec_normal.add(vec2_negative).get_y() == 1
    assert vec_normal.add(vec2_negative).get_z() == 9

def test_add_wrong_type(vec_normal, vec3_wrong):
    with pytest.raises(TypeError):
        vec_normal.add(vec3_wrong)

def test_add_zero(vec_normal, vec8_zero):
    assert vec_normal.add(vec8_zero).get_x() == 2
    assert vec_normal.add(vec8_zero).get_y() == 3
    assert vec_normal.add(vec8_zero).get_z() == 5


def test_sub(vec_normal, vec2_negative):
    assert vec_normal.sub(vec2_negative).get_x() == 1
    assert vec_normal.sub(vec2_negative).get_y() == 5
    assert vec_normal.sub(vec2_negative).get_z() == 1

def test_sub_wrong_type(vec_normal, vec3_wrong):
    with pytest.raises(TypeError):
        vec_normal.sub(vec3_wrong)

def test_sub_zero(vec_normal, vec8_zero):
    assert vec_normal.sub(vec8_zero).get_x() == 2
    assert vec_normal.sub(vec8_zero).get_y() == 3
    assert vec_normal.sub(vec8_zero).get_z() == 5

def test_sub_negative(vec6_k, vec7_k):
    assert vec6_k.sub(vec7_k).get_x() == -4
    assert vec6_k.sub(vec7_k).get_y() == -6
    assert vec6_k.sub(vec7_k).get_z() == -8