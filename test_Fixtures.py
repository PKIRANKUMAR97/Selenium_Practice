import pytest
import math

@pytest.fixture()
def input_value():
    value = 50
    return value

def test_diff(input_value):
    assert 150 - 100 == input_value

def test_mul(input_value):
    assert input_value * 2 == 1000
