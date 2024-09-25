"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

line = "short sentencing"

for x in line:
    # Creates for loop that iterates through every character in the string
    print(x)


"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

number_line = [1,2,5,6]
# Creates list with integers
start = 0

for x in number_line:
    # Creates for loop to iterate through the list
    start += x
    # Adds x (current item) to starting number
print(start)


"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

fahren_start = "Its a pleasure to burn"

for x in fahren_start.split(" "):
    # Iterates through every item separated by a space using the split function
    print(len(x))
    # Prints the length of each word


"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""

library = { 
    "charlottes web": "eb white",
    "handmaids tale": "margaret atwood",
    "atonement": "ian mcewan",
    "orient express": "agatha christie"
}
# Creates dictionary with four pairs

for x in library:
    # Iterates through dictionary
    print(x)

# I noticed that the loop only printed the keys and not the values. I did not expect this as I though that it would print both the keys and values. 