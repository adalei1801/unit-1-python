print("Behold! The Calculatinator-inator 9000! It calculates two numbers including decimals")

first_num = float(input("Enter a number: "))
sec_num = float(input("Enter a second number: "))
# Asks the user for two numbers and converts them into floats

print("Select an operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Exponential")
print("7. Remainder")
# Asks the user to select an operation and provides a list of choices

op_choice =  input("Select your operation: ")
# Asks the user to select an operation and allows them to make an input

if op_choice == "1":
    output = first_num + sec_num
    # If the user chooses addition, the program adds the numbers
elif op_choice == "2":
    output = first_num - sec_num
     # If the user chooses subtraction, the program subtracts the numbers
elif op_choice == "3":
    output = first_num * sec_num
     # If the user chooses multiplication, the program multiples the numbers
elif op_choice == "4":
    output = first_num / sec_num
     # If the user chooses division, the program divides the numbers
elif op_choice == "5":
    output = first_num // sec_num
     # If the user chooses floor division, the program divides the numbers and rounds them to the nearest and smallest integer
elif op_choice == "6":
    output = first_num ** sec_num
     # If the user chooses exponential, the program raises the first number to the power of the second number
elif op_choice == "7":
    output = first_num % sec_num
     # If the user chooses remainder, the program divides the numbers and returns the remained

print("The answer is: ", output)
# Prints the output of the choosen operation

