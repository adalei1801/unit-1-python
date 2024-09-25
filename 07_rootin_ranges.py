"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

for x in range(1,11):
    print(x)
    # Creates loop that iterates and prints numbers 1-10 

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

for x in range(900, 1001, 10):
    print(x)
    # Loop that iterates and prints numbers from 900-1000 in increments of 10

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

for x in range(1, 101, 9):
    print(x)
    # Loop statement that prints all numbers from 1 to 100 in increments of 9

"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

count = 0

for x in range(1,11):
    count += x
    # Creates loop that iterates all of the numbers in between 1-10 and adds them all together
print(count)


"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5

for i in range(rows):
     for j in range(i + 1):
         print('*', end=' ')
     print()

# The rows variable sets the amount of iterations for the loop to go through. The second for loop adds an asterisk for every iteration value (so the first iteration which totals to 0 gets 1 asterisk as 1 is added to the i).