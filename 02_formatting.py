"""
TASK 1:
Write code that checks if a user entered the correct password.
The password should not be case sensitive

"""

password = "bluebell"
pass_attempt = input("Whats the Password?: ").lower()
# Asks user for password and modifies the input to be all lower case

if pass_attempt == password:
    print("Correct!")
    # Creates condition for the input matching the password and prints "Correct!" if the attempt and password matches.
else:
    print("Incorrect!")
    # Creates else statement that prints "Incorrect!"if the user's input and the password do not match.


"""
TASK 2:
Write code that checks if a user inputs an empty string
If the string is empty, print "invalid" otherwise print "valid"
"""

word = input("Write something: ").strip()
# Asks the user to write something and strips any extra space at the start and end of the string. 

if word == "":
    print("Invalid!")
    # Creates an if statement for when the "word" string is empty (just having spaces also counts as empty) the program will print "Invalid!"
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
# Replaces all instances of the word "cat" with "dog" in the user's input
print(new_mad_lib)

"""
TASK 4:

Write a program that takes a person's name and age as input and prints it
"""

name_input = input("What is your name? ")
# Asks user for their name
age_input = input("What is your age? ")
# Asks user for their age
info = "Your name is {0} and you are {1}!".format(name_input, age_input)
# Formats the string by replacing the placeholders with the variables in the format function
print(info)

"""
TASK 5:

Write a program that takes in two floats, and prints the quotient
The result should be rounded to the nearest tenth (1 decimal place)
"""

decim_one = float(input("Write a decimal number: "))
# Asks the user for a decimal number and converts the input into a float
decim_two = float(input("Write another decimal number: "))
# Asks the user for a second decimal number and converts the input into a float

operation_quo = decim_one / decim_two
# Divides the two decimal numbers the user inputted

result = f"The result of the division is {operation_quo:.1f}"
# Formats the results of the division into the sentence by filling the placeholder with the quotient and rounds the quotient to the tenth (one decimal place).

print(result)


