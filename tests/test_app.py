from myapp.app import add, subtract, wrongMultiply, increment
import pytest
import pytest_check as check

def test_add():
    """Tests the additional function."""
    check.equal(add(2, 3), 5)

def test_subtract():
    """Tests the subtraction function."""
    check.equal(subtract(5, 3), 2)

def test_multiply():
    """Tests the multiply function."""
    check.equal(wrongMultiply(5, 3), 15)

def test_increment():
    """Tests the subtraction function."""
    check.equal(increment(5), 5 + 1)