# Exception Handling

'''Exception handling in Python is done using the try-except block to catch and handle runtime errors, preventing program crashes.'''

# Basic Exception handling

try:
    x = 10 / 0  # Division by zero
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

'''---------------------------------------------------------------------------------------------------------------------------------'''

# Generic exception

try:
    y=10/0
except Exception as e: #  Exception is super class
    print(f"{e.__class__.__name__}") # name of the exception

'''---------------------------------------------------------------------------------------------------------------------------------'''

# Handling multiple exceptions

try:
    num = int(input("Enter a number: "))  # May cause ValueError
    result = 10 / num  # May cause ZeroDivisionError
except ValueError: 
    print("Error: Invalid input! Please enter a number.")
except (ZeroDivisionError, AttributeError): # Multiple exception at same time
    print("Error: Division by zero is not allowed.")
except Exception as e: #  Exception is super class # This must be at the end coz it is default
    print(f"{e.__class__.__name__}") # name of the exception

# It is checking in one by one if first exception matches then it won't check other exceptions.

'''----------------------------------------------------------------------------------------------------------------------------------'''

# exception with else - else block will excecute when no exception excuted.
# The else block runs only if no exception occurs.
# It is like else with break with statement

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")  # Runs only if no exception occurs
finally:
    print(f"Always execute") # It is always excute whether exception execute or not.
# It is executed always like print 

'''------------------------------------------------------------------------------------------------------------'''

# custom exception handling
class NegativeNumberError(Exception):
    pass

def check_num(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers not allowed")

try:
    check_num(-10)
except NegativeNumberError as e:
    print(e)

'''------------------------------------------------------------------------------------------------------------'''

# Nested try except

try:
    x = int("abc")
except ValueError:
    try:
        x = int(input("Enter a valid number: "))
    except ValueError:
        print("Still invalid input")


