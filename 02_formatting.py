"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""

password = "bluebell"
pass_attempt = input("Whats the Password?: ").lower()
# Asks user for password and converts input into lower case

if pass_attempt == password:
    print("Correct!")
    # Creates condition for the input matching the password and prints "Correct!" if the attempt and password matches.
else:
    print("Incorrect!")
    # If input does not match the password, "Incorrect!" is printed


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

word = input("Write something: ").strip()

if word == "":
    print("Invalid!")
    # Creates if statment for the "word" string being empty, the user will be told the input is invalid
else: 
    print("Valid!")
    # Creates else statment so if the "word" string is not empty, the program will print "Valid!"

"""
TASK 3:

Write a program that will replace the word "cat" with the word "dog"
It should replace all occurances regardless of captilization 
"""

mad_lib = input("Write something about pets: ").lower()
# Asks the user for input about pets and changes answer into lowercase
new_mad_lib = mad_lib.replace("cat", "dog")
# Replaces all instances of the word "cat" with "dog"
print(new_mad_lib)


"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""

name_input = input("What is your name? ")
# Asks user for their name
age_input = str(input("What is your age? "))
# Asks user for their age
info = "Your name is {0} and you are {1}!".format(name_input, age_input)
print(info)
"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

decim_one = float(input("Write a decimal number: "))
decim_two = float(input("Write another decimal number: "))
# Ask the user for a decimal numbers

operation_quo = decim_one / decim_two
# Divides the numbers the user inputted

result = f"The result of the division is {operation_quo:.1f}"
# Formats the results of the division into a sentence and rounds the quotient to the tenth.

print(result)


