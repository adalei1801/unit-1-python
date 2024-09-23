'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

number = int(input("Enter a number: "))
# Asks user for a number and converts it to an integer

num_mod = number % 2
# Finds remainder of input when divided by 2

if num_mod == 0 and number > 10: 
    print("True")
    # If remainder is 0 and the input it greater than 10, Python prints "True"
else:
    print("False")
    # If above conditions are not met, Python prints "False"


'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age = int(input("How old are you? "))
# Asks user for age
student_status =  input("Are you a student? Yes or No? ").lower()
# Asks user for student status and converts answer to lowercase

if age < 18 or student_status == "yes":
    print("The price is $10")
    # If the user is not 18 and a student the price is $10
else: 
    print("The price is $20")
    # If the above condition is not met the price is $20 

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

fruit_list = ["watermelon", "apple", "grape", "pear"]
fruit_input = input("Name a fruit: ").lower()
# Asks the user to name a fruit and puts the answer in lowercase

if fruit_input in fruit_list:
    print("Yes, that fruit is in the list.")
    # If user input is in the list then Python prints that the fruit is in the list
else:
    print("No, that fruit is not in the list.")
    # If the input is not in the list, the user is told that it is not there

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

year = int(input("Enter a year: "))
# Asks the user for a year
year_cent = year % 100
# Finds remainder of year divided by 100
year_leap = year % 4
# Finds remainder of year divided by 4

if year_cent == 0 and year_leap == 0:
    print("This year is a century and leap year")
    # If the year divided by 100 and 4 has no remainder then its a century and leap year and Python will print that
elif year_cent == 0 and year_leap != 0:
    print("This year is a century year")
    # If the year divided by 100 has no remainer but the year divided by 4 does than the year being a century year will be printed.
elif year_cent != 0 and year_leap == 0:
    print("This year is a leap year")
    # If the year divided by 4 has no remaineder but the year divided by 100 does the year is a leap year and Python will print that.
else: 
    print("This year is not a leap year or a century year")
    # If nonre of the above conditions are met than the year is not a century or leap year and the user will be told


'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

weight = int(input("Enter package weight (in kg): "))
# Asks for weight in lgs
destination = input("Enter destination zone: ").upper()

weight_cost_a = str(weight * 5)
weight_cost_b = str(weight * 7)

if destination == "A":
    print("Your total is $" + weight_cost_a)
elif destination == "B":
    print("Your total cost is $" + weight_cost_b)
else:
    print("Total cannot be calculated due to destination error")

if weight < 0:
    print("Error, package cannot be 0 kgs")

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

side_a = int(input("Enter side length a: "))
side_b = int(input("Enter side length b: "))
side_c = int(input("Enter side length c: "))

if side_a == side_b and side_b == side_c:
    print("Your triangle is an equilateral")
elif side_a == side_b and side_b != side_c:
    print("Your triange is an isosceles")
elif side_a != side_b and side_b != side_c:
    print("Your triange is a scalene")
else:
    print("This is not a triangle")