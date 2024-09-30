with open("task_list.txt") as file:
    task_list = file.readlines()
    print(task_list)
    # Opens and reads text file that will hold the list

while True: 
    if task_list == []:
        # If statements runs if task list is empty and provides the user a way to add tasks
        print(" ")
        print("-------------------------------")
        print(" ")
        print("You do not have any current tasks")
        ask_task = input("Would you like to add one? ").lower()
        # Asks user if they want to add a task and converts input into lowercase
        if ask_task == "yes":
            # If statement for the user replying yes to previous question
            new_task = input("What is your new task? ")
            task_list.append(new_task + "\n")
            # Asks user for new task and adds input to the task list using append function
            print(" ")
            print("-------------------------------")
            print(" ")
        elif ask_task == "no":
            print("Alright, please input a task when you are ready")
            # Elif statment for the user saying no to adding a task 

    else:
        print("-------------------------------")
        print(" ")
        print("Your current task(s) are: ")
        for x in task_list:
            item_index = task_list.index(x) + 1
            print(item_index, ")", x)
             # Loop statement that orgainzes list items by line and prints it for the user
        print(" ")
        ask_task = input("Would you like to add, remove, or edit one? Or would you like to close the program? ").lower()
        # Asks user to add or remove a task and converts answer to lowercase
        print(" ")
        print("-------------------------------")

        if ask_task == "add":
            # If statement for the user adding a task
            print(" ")
            new_task = input("What is your new task? ")
            print(" ")
            task_list.append(new_task + "\n")
            # Asks user for new task and adds task to the list. It also puts the task on a new line in the text file
        elif ask_task == "remove":
            # Elif statement for the user removing an item
            print("Your tasks are:")
            for x in task_list:
                item_index = task_list.index(x) + 1
                print(item_index,")", x)
                # Loop statement that formats list items by line and numbers them. Also prints current tasks
    
            remove_task = int(input("Which task would you like to remove (by number)? "))
            # Prints task list and asks the user what they want removed and converts input into lowercase
            print(" ")
            del task_list[remove_task - 1]
                # Removes task from list
            print("-------------------------------")
            print(" ")
        elif ask_task == "edit":
            # Sets up elif statement for the user choosing edit
            print("Your tasks are:")
            for x in task_list:
                item_index = task_list.index(x) + 1
                print(item_index, ")", x)
                # Prints current task list and numbers the items
            edit_task = int(input("What task would you like to edit (by number)? "))
            # Asks the user for what task they want changed and converts input into an integer
            change_task = input("What do want to change it to? ")
            # Asks user what they want to change it too
            task_list[edit_task - 1] = change_task
            # Assigns the new task to the old task's index

        elif ask_task == "close":
            with open("task_list.txt", "w") as file:
                file.writelines(task_list)
                # Opens text file that holds the list and writes the list into file
            
            break
            # Exits program after list is saved to file

        else:
            print("Sorry, I do not understand, please try again")
            # Else statement for incorrect input and allows user to try again
