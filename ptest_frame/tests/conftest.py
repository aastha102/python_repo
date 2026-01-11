"""
Pytest Fixtures Module for Rectangle Test Objects.

This module defines reusable pytest fixtures that provide Rectangle
instances for unit testing purposes. The fixtures supply predefined
rectangle objects with specific dimensions, enabling consistent and
maintainable test setups across multiple test modules.

Fixtures:
- my_rectangle:
  Provides a Rectangle instance with a width of 10 and a height of 20.
  Used for validating standard rectangle behavior such as area and
  perimeter calculations.

- weird_rectangle:
  Provides a Rectangle instance with a width of 20 and a height of 30.
  Used for testing scenarios involving non-standard dimensions or
  object comparison.

Pytest Features Used:
- pytest.fixture: For defining reusable test setup logic.

Dependencies:
- pytest: Testing framework.
- source.shapes: Module under test containing the Rectangle class.

Usage:
- These fixtures can be imported directly into test modules or placed
  in a `conftest.py` file to make them automatically available to all
  tests within the test suite.

Notes:
- Using fixtures improves test readability and reduces code duplication.
- Fixture scopes can be extended (e.g., function, module, session)
  based on testing requirements.

Author:
- Test suite maintained by the QA/Automation team.

"""
import source.shapes as shapes
import pytest


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(20, 30)