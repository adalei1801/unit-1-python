"""
text = "Hello, world, my name is"
count = 0

for char in text:
    # Creates loop to iterate through every character in the string
    if char == " ":
       count += 1
        # Creates if statement for when the string is empty the count variable increases by 1.
       # This is where the problem arises as the if statement runs when the string is empty, not when the string is empty, so the quotation marks needed a space.

print(count)
"""

"""
print("give me a number")
n = int(input())
# Asks the user for input and converts the input into a integer
# Issue 1 arose as the for loop would not iterate using a string while doing math

for num in range(1, n + 1):
# Creates for loop to go through every number from 1 to the user's input
# Issue 2 rises as the loop would not iterate the user's number as the second number in a range function does not get iterated.
    if num % 2 == 0:
    # Creates if statment for the current number being even if its remainder after being divided by 2 equals zero. 

    # Previously the equality sign was a less than sign which needed to be changed as numbers with remainders greater than 0 after being divided by 2 are odd, so the condition would not be met and even numbers would be printed as odd.
        print(num, "is even.")
    else:
        print(num, "is odd.")
        # Creates else statment for odd number if their remainder from being divided by 2 is greater than 0.
"""

"""
num = int(input("Enter an integer: "))

if num < -1:
  print("No negative numbers.")
  # Creates if statment for num being greater than -1, the program will print no negative numbers.
else:
  result = 1
  # Creates else statement for numbers that are positive or 0 to compute their factorial
  for i in range(1, num + 1):
    result *= i   
    # Creates for loop that iterates through number one to use input and multiply the result by the iterated number and assigns the new number to result variable. 
    # Issue arises as the second number in a range function is exclusive and will not be iterated on, which means the factorial cannot be calculated properly as they are the number multiplied by every number from 1 to itself.

    # So, a "+ 1" must be added so the excluded number is one more than the input, which will allow the factorial to be calculated properly as the input is included.

  print("Factorial of ", num, "is", result)
  # Prints the final result in a sentence

  # Print statements do not concatenate strings and integers. To solve this problem, commas must be used to separate the strings and the integers as it allows the program to print several things without concatenating them.
"""

attempts = 0
correct_password = "secret"

while True:
    # Creates while loop that allows users to input password after correct attempts while condition is True.
    password = input("Enter your password: ")
    # Asks the user for the password
    attempts += 1
    # Increases the amount of attempts by 1

    if password == correct_password:
        print("Correct password!")
        break
        # Creates if statement for when the attempt equals the password Python will print correct password and end the program.

        # There were two issues with the code. One, if the guess equaled "incorrect_password", the program will print "Correct password!" which is wrong as incorrect_password is not the password. This needed to be changed to password == correct_password so when the attempt equaled the password the program will print correct accurately.

        # Second, even if the password is right, the program still runs. To fix this a break statement needs to be added.
    else:
        print("Incorrect password")
        # Creates else statement for when the attempt is incorrect

    if attempts == 3:
        print("Too many attempts")
        break
    # Creates if statement for the user trying too many times (when attempts equal 3), the program will print that there has been "too many attempts" and break the loop

    # The issue with this statement is that it allows the user to try four times and not three as attempts needed to be greater than three for the statment to run. This was fixed by changing the condition to attempts == 3 as when the user tried 3 times the code would print that there were "too many attempts" and break.