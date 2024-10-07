"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
from datetime import datetime
# Imports the datetime component from the datetime module

current_datetime = datetime.now()
# Uses the now function from the datetime component to get the current date and time and assigns it to a variable
print(current_datetime)

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

date_time = datetime.now()
# Uses now function to get the current date and time and assigns date and time to a variable

format_date = date_time.strftime("%m/%d/%Y")
# Formats "date_time" variable into American date format using strftime function
print(format_date)

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

date_one = "05/06/2007"
date_two = "10/07/2024"
# Sets two dates in strings

format_one = datetime.strptime(date_one, "%m/%d/%Y")
format_two = datetime.strptime(date_two, "%m/%d/%Y")
# Formats the string datas into the American date format using the strptime function

print(format_two - format_one)
# Prints the difference between the two dates

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

birthdate = input("What is your birthdate? Input in MM/DD/YYYY format: ")
# Asks user for their birthday as input
today = datetime.now()
# now function gets today's date and time and assigns it to a variable

format_birthdate = datetime.strptime(birthdate, "%m/%d/%Y")
# Formats the user's input using the strptime function
day_age = today - format_birthdate
# Subtracts today's date and user input to get the user's age

print("You are ", day_age, " old")
# Prints message telling the user their age in days
