"""
Test Module for my_func Arithmetic Operations using Pytest.

This module contains unit tests for the functions defined in
`source.my_func`, specifically focusing on addition and division
operations. The tests are written using the pytest framework and
demonstrate various pytest features such as exception handling,
test skipping, expected failures, and performance-related testing.

Covered Test Scenarios:
- Validation of integer addition.
- Validation of division with positional and keyword arguments.
- Handling of division by zero using pytest.raises.
- Support for string concatenation using the add function.
- Verification of slow-running tests.
- Demonstration of skipped tests for known broken functionality.
- Demonstration of expected failures (xfail) for unresolved defects.

Pytest Features Used:
- pytest.raises: To validate exception handling.
- pytest.mark.skip: To skip tests that are currently broken or disabled.
- pytest.mark.xfail: To mark tests that are expected to fail.
- Assertions: To validate expected outcomes.

Dependencies:
- pytest: Test execution and assertions.
- time: Used to simulate a slow-running test.
- source.my_func: Module under test.

Notes:
- Some tests are intentionally skipped or marked as expected failures
  to document known issues without failing the test suite.
- Slow tests may be excluded from regular test runs using markers
  if needed in the future.

Author:
- Test suite maintained by the QA/Automation team.

"""
import source.my_func as my_func
import time
import pytest

def test_add():
    result=my_func.add(1,5)
    assert result==6

def test_div():
    result=my_func.div(num2=2,num1=10)
    assert result==5

def test_div_by_0():
    with pytest.raises(ZeroDivisionError):
        my_func.div(num2=0,num1=10)
  
def test_add_strings():
    result=my_func.add(num1="Pytest ", num2="Framework")
    assert result == "Pytest Framework"

def test_very_slow():
    time.sleep(3)
    result=my_func.div(10,5)
    assert result ==2

@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    assert my_func.add(1,2)==3

@pytest.mark.xfail(reason="This feature is currently broken")
def test_divide_by_0():
    my_func.div(1,2)