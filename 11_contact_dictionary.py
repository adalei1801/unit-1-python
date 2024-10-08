address_book = dict()
# Creates empty dictionary

while True:
    # Sets while loop for the program to run as long as needed
    print("-------------------------")
    print("Contact Menu:")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. List Contacts")
    print("4. Exit")
    # Prints list of the user's options
    choice = input("What would you like to do? ")
    # Asks the user to choose from menu
    print("-------------------------")

    if choice == "1" or choice == "add":
        # Sets if statement for the user chosing to add a contact
        new_contact =  input("What is the person's name: ")
        new_number = input(f"What is {new_contact} phone number? ")
        # Asks user for name and phone number. When asking for a phone number, the question is formatted to include the user's name.

        if len(new_number) < 10:
            # Sets if statement that checks the length of the phone number and checks for the phone number having less than ten characters
            print("This phone number is not valid, its too short, please try again")
            continue
            # Restarts loop if phone number is to short

        address_book[new_contact] = new_number
        # Adds user inputs to dictionary
        if new_contact not in address_book:
            # Sets if statement for the name not being in the dictionary already
            print("This name is taken, try again")
            continue
            # Checks if name is in dictionary and reruns the code if it is
        print("-------------------------")

    elif choice == "2" or choice == "delete":
        # Creates elif statement for the user chosing to delete a contact
        if len(address_book) == 0:
            # Creates if statement for the dictionary being empty
            print("You do not have any contacts, please try again")
            continue 
            # Restarts loop if there are no contacts
        del_name = input("Who would you like to delete? ")
        # Asks the user for who they want deleted

        if del_name not in address_book:
            # Sets if statement for the input not being in dictionary
            print("This contact does not exist, try again")
            continue
            # Restarts code if user input is not in dictionary

        del address_book[del_name]
        # Deletes contact from dictionary

    elif choice == "3" or choice == "list":
        # Creates elif statement for the user choosing to list the dictionary
        print("Name - Phone Number")
        for x in address_book:
            print(f"{x} - {address_book[x]}")
            # Sets for loop to print the dictionary in formatted way

    elif choice == "4" or choice == "exit":
        # Sets elif statement for the user choosing to exit
        print("Goodbye! I hope you call again")
        break
        # Breaks the code if the user exits the program



