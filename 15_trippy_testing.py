"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b
 
  
try:
    assert divide(-1,0) == -1/8
except:
   print("Error")
# Extra credit work: create an AssertionError, but keep the program running # I used try/expect statements to print "Error" if the code in the try statement has an error

assert divide(2,4) == 0.5
# Checks that the divide function will return 0.5 when dividing 2 and 4
assert divide(4,0) == None
# Tests whether the divide function will return none when dividing 4 and 0


"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
        return 1
  else:
        return n * factorial(n - 1)


assert factorial(5) == 120
# Checks whether or not the function will return 120 if the argument equals 5
assert factorial(0) == 1
# Tests for the function returning 1 when the argument equals 0

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

assert reverse_string("Bell") == "lleB"
# Tests that the function will return the argument spelled backwards
assert reverse_string("Hello") == "olleH"
# Tests for the function returning the argument string backwards

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

assert fibonacci(-2) == 0
# Validates that the function will return 0 if the number is negative
assert fibonacci(1) == 1
# Tests whether the function will return one if the argument equals 1
assert fibonacci(6) == 8
# Checks whether the function will return 8 if the argument equals 6

"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None

assert is_valid_email("ashleymking567@gmail.com") == True
# Checks if the function will return True if the given email is valid
assert is_valid_email("ashl kn7@gail.com") == False
# Validates that the function will return False is the email given is invalid



