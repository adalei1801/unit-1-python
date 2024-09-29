with open("task_list.txt") as file:
    task_list = file.readlines()
    print(task_list)

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
            task_list.append(new_task)
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
             # Loop statement that orgainzes list items by line
        print(" ")
        ask_task = input("Would you like to add, remove, or edit one? ").lower()
        # Asks user to add or remove a task and converts answer to lowercase
        print(" ")
        print("-------------------------------")

        if ask_task == "add":
            # If statement for the user adding a task
            print(" ")
            new_task = input("What is your new task? ")
            print(" ")
            task_list.append(new_task)
            # asks user for new task and adds task to the list
        elif ask_task == "remove":
            # Elif statement for the user removing an item
            print("Your tasks are:")
            for x in task_list:
                item_index = task_list.index(x) + 1
                print(item_index,")", x)
                # Loop statement that orgainzes list items by line
    
            remove_task = int(input("Which task would you like to remove (by number)? "))
            # Prints task list and asks the user what they want removed and converts input into lowercase
            print(" ")
            del task_list[remove_task - 1]
                # Removes task from list
            print("-------------------------------")
            print(" ")
        elif ask_task == "edit":
            print("Your tasks are:")
            for x in task_list:
                item_index = task_list.index(x) + 1
                print(item_index, ")", x)
            edit_task = int(input("What task would you like to edit (by number)? "))
            change_task = input("What do want to change it to? ")
            task_list[edit_task - 1] = change_task
            
        else:
            print("Sorry, I do not understand, please try again")
            # Else statement for incorrect input and allows user to try again
