"""
This module contains tests for the calculator operations and Calculation class.

The tests are designed to verify the correctness of basic arithmetic operations
(addition, subtraction, multiplication, division) implemented in the calculator.operations module,
as well as the functionality of the Calculation class that encapsulates these operations.
"""

# Import statements:
# Disable specific pylint warnings that are not relevant for this test file.
# Import the Decimal class for precise arithmetic, which is especially useful in financial calc.
# Import pytest for writing test cases.
# Import the Calculation class from the calculator package to test its functionality.
# Import the arithmetic operation functions (add, subtract, multiply, divide) to be tested.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, divide#, subtract, multiply

# pytest.mark.parametrize decorator is used to parameterize a test func, enabling it to be called
# with diff sets of arguments. Here, it's used to test various scenarios of arithmetic operations
# with both int and float operands to ensure the operations work correctly under diff conditions.

def test_calculation_operations(a, b, operation, expected):
    """
    Test calculation operations with various scenarios.
    
    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('a' and 'b'),
    and that the result matches the expected outcome.
    
    Parameters:
        a (Decimal): The first operand in the calculation.
        b (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    # Create a Calculation instance with the provided operands and operation.
    calc = Calculation(a, b, operation)
    # Perform the operation and assert that the result matches the expected value.
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    
    This test verifies that the __repr__ method of a Calculation instance returns a string
    that accurately represents the Calculation object, including its operands and operation.
    """
    # Create a Calculation instance for testing.
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    # Define the expected string representation.
    expected_repr = "Calculation(10, 5, add)"
    # Assert that the actual string representation matches the expected string.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match."

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero 
    is mathematically undefined and should be handled as an error.
    """
    # Create a Calculation instance with a zero divisor.
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    # Expect a ValueError to be raised.
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        # Attempt to perform the calculation, which should trigger the ValueError.
        calc.perform()
