from myapp.app import add, subtract, wrongMultiply, increment
import pytest

def test_add():
    """Tests the additional function."""
    assert add(2, 3) == 5

def test_subtract():
    """Tests the subtraction function."""
    assert subtract(5, 3) == 2

@pytest.mark.xfail
def test_multiply():
    """Tests the multiply function."""
    assert wrongMultiply(5, 3) == 15

def test_increment():
    """Tests the subtraction function."""
    assert increment(5) == 5 + 1