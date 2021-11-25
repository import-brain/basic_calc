"""
unit tests for major functions in calc.py
"""
# import functions from calc.py
from calc import (
    add, 
    subtract, 
    multiply, 
    divide, 
    exponent,
)

# title function for each suite of tests
def test_title(test):
    print(test + " tests")
    print("--------------------")

def separator():
    print("\n")
    print("--------------------")

# adding tests
def add_tests():
    test_title("add")

    try:
        assert add(1, 2) == 3
        assert add(1, 4) == 5
        assert add(1, -4) == -3
    except AssertionError:
        print("Adding tests failed, check your code")
        separator()
        return 1
    else:
        print("Adding tests passed")
        separator()
        return 0
# subtract tests
def subtract_tests():
    test_title("subtract")

    try:
        assert subtract(3, 7) == -4
        assert subtract(1, 4) == -3
        assert subtract(1, -4) == 5
        assert subtract(0, 0) == 0
    except AssertionError:
        print("Subtracting tests failed, check your code")
        separator()
        return 1
    else:
        print("Subtracting tests passed")
        separator()
        return 0
# multiply tests
def multiply_tests():
    test_title("multiply")

    try:
        assert multiply(2, 3) == 6
        assert multiply(1, 4) == 4
        assert multiply(1, -4) == -4
        assert multiply(0, 5) == 0
    except AssertionError:
        print("Multiplying tests failed, check your code")
        separator()
        return 1
    else:
        print("Multiplying tests passed")
        separator()
        return 0

def divide_tests():
    test_title("divide")

    try:
        assert divide(6, 3) == 2
        assert divide(4, 1) == 4
        assert divide(1, -4) == -0.25
        assert divide(0, 5) == 0
    except AssertionError:
        print("Dividing tests failed, check your code")
        separator()
        return 1
    else:
        print("Dividing tests passed")
        separator()
        return 0

def exponent_tests():
    test_title("exponent")

    try:
        assert exponent(2, 3) == 8
        assert exponent(1, 4) == 1
        assert exponent(1, -4) == 1
        assert exponent(0, 5) == 0
        assert exponent(2, 0) == 1
        assert exponent(9, 0.5) == 3.0
    except AssertionError:
        print("Exponent tests failed, check your code")
        separator()
        return 1
    else:
        print("Exponent tests passed")
        separator()
        return 0
# call all test functions
add_tests()
subtract_tests()
multiply_tests()
divide_tests()
exponent_tests()