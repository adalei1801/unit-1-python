"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""


num = 1

while num < 11:
    # Creates loop that runs as long as num is less than 11
    print(num)
    num += 1
    # Increases "num" by 1


"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

number_ten = 10

while number_ten > 0:
    # Creates while statment that runs as long as "number_ten" is greater than 0
    print(number_ten)
    number_ten -= 1
    # Subtracts 1 from "number_ten"

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

result = 1
factor = int(input("Enter a number: "))
# Asks user for input and converts it into an integer

while factor > 0:
    # Creates while loop that runs as long as "factor" is greater than 0
    result = result * factor
    # Multiples the result variable by the user's input
    factor -= 1
    # Decreases factor variable by 1
print(result)

    

"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

password = "daydream"

guess = input("Whats the password? ")
# Asks user for password guess

while guess != password:
    # Sets while loop to run while the user's guess and password do not match
    print("wrong")
    guess = input("Whats the password? ")
     # Allows the user to try again if the guess is wrong
else: 
    print("Correct!")
    # Else statement prints correct if user is right

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

user_num = int(input("Enter a number: "))
# Asks user for a number and converts it into an integer

prev_num = 0
current = 1

while user_num > 0:
    # Creates while loop for as long as the user input is greater than 0
    print(current)
    current = prev_num + current
    # Adds the current number to the previous number in the sequence
    prev_num = current - prev_num
    # Subtracts previous number from current number and assigns the value to the prev_num variable
    user_num -= 1
    # Subtracts 1 from the user_num variable
