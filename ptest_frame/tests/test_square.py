"""
Pytest Test Module for Square Shape Area and Perimeter Calculations.

This module contains parameterized unit tests for validating the area
and perimeter calculations of the Square class defined in `source.shapes`.
The tests ensure that square dimensions are handled correctly for multiple
input values using data-driven testing.

Test Coverage:
- Verifies correct area calculation for squares with different side lengths.
- Verifies correct perimeter calculation for squares with different side lengths.
- Confirms that square behavior is consistent when initialized with equal
  length and width values.

Pytest Features Used:
- pytest.mark.parametrize: Used to run the same test logic with multiple
  sets of input values for improved coverage and reduced code duplication.
- Assertions: To validate expected outcomes.

Dependencies:
- pytest: Testing framework used to execute the tests.
- source.shapes: Module under test containing the Square class.

Assumptions:
- The Square class accepts length and width as constructor arguments.
- The Square class implements `area()` and `perimeter()` methods.
- Passing equal values for length and width represents a valid square.

Notes:
- Parameterized tests improve maintainability and scalability by allowing
  easy extension of test cases.
- These tests are pure unit tests and do not rely on external systems.

Author:
- Test suite maintained by the QA/Automation team.

"""
import source.shapes as shape
import pytest

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4,16), (9,81)])
def test_multiple_square_areas(side_length, expected_area):
    assert shape.Square(side_length, side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(4, 16), (5,20), (9,36)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    assert shape.Square(side_length, side_length).perimeter() == expected_perimeter

