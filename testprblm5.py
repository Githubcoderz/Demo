import pytest
import math

@pytest.fixture
def Data():
    return [1, 2, 3]

# Test for sum
def test_sum(Data):
    assert sum(Data) == 6

def test_product(Data):
    product = math.prod(Data)
    assert product == 6