"""
Pytest Test Module for Rectangle Shape Functionality.

This module contains unit tests for the Rectangle class defined in
`source.shapes`. The tests verify the correctness of rectangle-related
operations such as area calculation, perimeter calculation, and object
comparison.

Test Coverage:
- Validates that the area of a rectangle is calculated correctly.
- Validates that the perimeter of a rectangle is calculated correctly.
- Ensures that two rectangles with different dimensions are not equal.

Fixtures:
- my_rectangle: Provides a Rectangle instance with dimensions 10x20.
- weird_rectangle: Provides a Rectangle instance with dimensions 20x30.
  (Fixtures are expected to be defined in conftest.py or another test module.)

Pytest Features Used:
- Fixtures: For reusable test data setup.
- Assertions: To validate expected behavior.

Dependencies:
- pytest: Test framework used for execution.
- source.shapes: Module under test containing the Rectangle class.

Notes:
- Fixture definitions are intentionally commented out in this module
  and may be provided globally via a conftest.py file.
- This test suite assumes that the Rectangle class implements
  area(), perimeter(), and equality comparison methods.

Author:
- Test suite maintained by the QA/Automation team.

"""

import source.shapes as shapes
import pytest


# @pytest.fixture
# def my_rectangle():
#     return shapes.Rectangle(10, 20)

# @pytest.fixture
# def weird_rectangle():
#     return shapes.Rectangle(20, 30)

def test_area(my_rectangle):
    
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter()== 2*(10+20)

def test_not_equal(my_rectangle, weird_rectangle):
    assert my_rectangle!=weird_rectangle
