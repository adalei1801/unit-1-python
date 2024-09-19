"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

colors = ["blue", "green", "purple", "red"]
# Creates a list with four colors
print(colors)

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

colors.append("yellow")
# Appends "yellow" to the end of the "colors" list
print(colors)

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

colors.remove("purple")
# Removes "purple" from "colors" list
print(colors)

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

colors[3] = "orange"
# Changes the color at the third index to "orange"
print(colors)

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

other_colors = ["white", "pink", "black"]
# Creates second list with three other colors
joined_colors = colors + other_colors
# Extends the "colors" list with the "other_colors" list's elements
print(joined_colors)

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

del joined_colors[4]
# Deletes the color at fourth index in the "joined_colors" list
print(joined_colors)

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

duo_colors = colors[0:2]
# Indexes the first two colors in the "colors" list and puts them into a new list 
print(duo_colors)

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

color_bow = duo_colors + joined_colors
# Extends the "duo_colors" list with the "joined_colors" list
print(color_bow)