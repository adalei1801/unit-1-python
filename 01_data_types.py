"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.
"""

point_val = 7.5 
point_num = int(point_val) 
# converts floating point into integer
print(point_val, point_num)
# prints the orginal floating point and its integer version


"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""

num_select = int(input("Type in a number: "))
# Asks for a number, allows user to input number, and converts input into integer

if num_select < 0:
    print("It's negative")
    # Creates an if statement for the input being less than zero and prints that the input is negative
elif num_select > 0:
    print("It's positive")
    # Creates an elif statement for the input being greater than zero and prints that the input is positive
else:
    print("It's zero")
    # Creates else statement for the input being zero and prints that the input is zero

"""
TASK 3:

Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""

first_int = int(input("Give me a number: "))
# Asks user to input a number and converts input into integer
second_point = float(input("Give me a decimal number: "))
# Asks user to input a decimal and converts the input into floating point

numbers_sum = first_int + second_point
# Adds the two inputs
numbers_diff = first_int - second_point
# Subtracts the two inputs
numbers_product = first_int * second_point
# Multiples the two inputs
numbers_quot = first_int / second_point
# Divides the two inputs

print(numbers_sum, numbers_diff, numbers_product, numbers_quot)
# Prints the products of the above operations
print("Sum, Difference, Product, and Quotient of your inputs")
# Prints message to differentiate and label numbers

"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""

fruit_supply = {
    "watermelons": 23,
    "grape bunches": 15
}
# Names the dictionary and gives it keys and values

print(fruit_supply["grape bunches"])
# Prints the value assigned to the key in the dictionary 

"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

strung_numbers = "26,79,91,84"
comma_split = strung_numbers.split(",")
# Deliminates the original string with commas and makes it a list
bowl_num = tuple(comma_split)
# Converts list into tuple and stores it in a variable
print(strung_numbers, bowl_num)
# Prints original string and tuple version