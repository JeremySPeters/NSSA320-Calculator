from ..src.pascaline import (
    add,
    subtract,
    divide,
    multiply
)


def test_add():
    assert add(5, 8) is 13


def test_subtract():
    assert subtract(9, 6) is 3


def test_divide():
    assert divide(10, 5) is 2


def test_multiply():
    assert multiply(7, 3) is 21