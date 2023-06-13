while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")

    if 'Add' in user_action:
        #initial prompt
        user_prompt = "Enter a todo: "
        task = input(user_prompt)+"\n"
        #accessing existing file
        # file = open("Files/todo.txt", 'r')
        # todos = file.readlines() #storing in a variable
        # file.close() #sometimes different parts of code try to acces the code so it needs to be closed
        ##change file opening procedure to 'with' clause so it automatically closes file
        with open("Files/todo.txt",'r') as file:
            todos = file.readlines()

        #appending the read input to the variable
        todos.append(task)
        #writing it back to the file
        file = open("Files/todo.txt", 'w')
        file.writelines(todos)
        file.close()
    if 'Show' is user_action:
        #opening the file in readmode
        # file = open("Files/todo.txt", 'r')
        # task = file.readlines()
        # file.close()
        ##change file opening procedure to 'with' clause so it automatically closes file
        with open("Files/todo.txt",'r') as file:
            task = file.readlines()
        #check if there are any tasks in the list
        if task:
            print(f"Your pending tasks are: ")
            # eliminating the "\n" from the end of the list
            newtasks = [item.strip("\n") for item in task]
            for index, item in enumerate(newtasks):
                print(f"{index + 1}-{item.strip()}")
        else:
            print("You have no pending tasks!")
    if 'Edit' in user_action:
        # file = open("Files/todo.txt", 'r')
        # task = file.readlines()
        ##change file opening procedure to 'with' clause so it automatically closes file
        with open("Files/todo.txt", 'r') as file:
            task = file.readlines()
        for index,item in enumerate(task):
            print(f"{index+1}-{item.strip()}")
        # file.close()

        user_input = int(input("Enter the task # to change: "))
        if user_input > len(task) or user_input<=0:
            print(f"Please Enter valid input from 1 to {len(task)}")
        else:
            user_edit_ = input(f"Change '{task[user_input-1]}' to: ")
            task[user_input-1] = user_edit_
            # file = open("Files/todo.txt", 'w')
            # file.writelines(task)
            # file.close()
            ##change file opening procedure to 'with' clause so it automatically closes file
            with open("Files/todo.txt", 'w') as file:
                file.writelines(task)
            print(f"Done!, Updated the info to {user_edit_}")

    if 'Complete' in user_action:
        with open("Files/todo.txt",'r') as file:
            task = file.readlines()
        #check if there are any tasks in the list
        if task:
            print(f"Your pending tasks are: ")
            # eliminating the "\n" from the end of the list
            todos = [item.strip("\n") for item in task]
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item.strip()}")
            number = int(input("Input the number of todo to complete: "))
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            with open("Files/todo.txt", 'w') as file:
                file.writelines("\n".join(todos)) #add new line on each time to register as different task
            # Display which item was removed from the list
            message = f"todo '{todo_to_remove}' removed from the list"
            print(message)
        else:
            print("You have no pending tasks!")

    if 'Exit' in user_action:
        break
    else:  # defined variable for outlier input
        print("Enter a valid input.")

with open("Files/todo.txt", 'r') as file:
    task = file.readlines()

if len(task) == 0:
    print(f"The list is blank")
else:
    print(f"List with {len(task)} item(s): {str.join(',' , list(i for i in task))}")
