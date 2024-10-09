"""
Task 1: Greeting
Write a function that takes a name as a 
parameter and prints a greeting message like "Hello, [name]!".
"""

def greet(name, salutations= "Salutations"):
    print(salutations + " " + name)
    # Function that prints a greeting using the above arguments

greet("Wilbur")
# Calls function with "Wilbur" filling in the argument


"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def squared(number):
    return number**2
# Function that squares a given number and returns that value

root = squared(4)
# Runs function using the number 4 and stores value in variable

"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""

def sorting(sort_num):
    # Function that determines whether a number is even or odd
    if sort_num % 2 == 0:
        return True
    # Creates if statement runs for the number being even and returns True
    else:
        return False
    # If the number is odd, the program will return False
    
sorted = sorting(5)
# Runs funciton using 5 and assigns value to variable

"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""

def area(length, width):
    return length*width
# Function that returns area of rectangle

rectangle = area(6,7)
# Calls function using 6 and 7 as arguments and stores value in variable


"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def cel_fah(cel):
    return (cel * 9/5) + 32
# Function that converts Celsius into Fahrenheit

fah = cel_fah(84)
# Calls function using 84 as function and assigns value to variable

"""
Task 6: Average of Numbers
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def average(select):
    for x in select:
        # For loop that iterates through the numbers in a list
        sum = sum + x
        # Adds current number and the sum and saves value to the sum variable
    
    return sum / len(select)
    # Returns average of numbers in list

listed_mean = average([2,5,7,6,3])
# Executes function using list as argument and saves value to variable


"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, and returns the total.
Your function should also optionally accept a 3rd argument for discount, and return the discounted if provided.
"""

def shop_calc(price, quant, discount=0):
    total = quant * price
    # Function that calculates price of purchase

    if discount > 0:
        total = total * (1 - discount)
        # If statement for the discount. Calculates new total using the discount

    return total
    # Returns the total

receipt = shop_calc(20, 2, 0.3)
# Executes function including the discount as a argument and saves value to variable

disc_receipt = shop_calc(20, 2)
# Executes the function without the discount as an argument and saves value to variable