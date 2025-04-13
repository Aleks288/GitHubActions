from myapp.app import add, subtract, wrongMultiply, increment
import pytest

def test_add():
    """Tests the additional function."""
    assert add(2, 3) == 5

def test_subtract():
    """Tests the subtraction function."""
    assert subtract(5, 3) == 2

def test_multiply():
    """Tests the multiply function."""
    a = wrongMultiply(5, 3)
    if a != 15:
        pytest.fail("Wrong answer")
    else:
        assert true

def test_increment():
    """Tests the subtraction function."""
    assert increment(5) == 5 + 1