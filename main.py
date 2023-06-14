while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        task = user_action[4:] #input like 'add go to gym - 'go to gym' gets added

        with open("Files/todo.txt",'r') as file:
            todos = file.readlines()
        #appending the read input to the variable
        todos.append(task.capitalize() + '\n')
        #writing it back to the file
        with open("Files/todo.txt",'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show') :
        #opening the file in readmode
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
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number-1
            with open("Files/todo.txt", 'r') as file:
                task = file.readlines()

            if number > len(task) or number<=0:
                print(f"Please Enter valid input from 1 to {len(task)}")
            else:
                user_edit_ = input("Enter the new todo: ")
                task[number] = user_edit_+"\n"
                with open("Files/todo.txt", 'w') as file:
                    file.writelines(task)
                print(f"Done!, Updated the info to '{user_edit_}'")
        except ValueError:
            print("Your command is not valid.")
            #give user the opportunity to enter the command again
            continue

    elif user_action.startswith('complete'):
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

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid, please keep the inputs as stated above")

with open("Files/todo.txt", 'r') as file:
    task = file.readlines()

if len(task) == 0:
    print(f"The list is blank")
else:
    print(f"List with {len(task)} item(s): {str.join(',' , list(i for i in task))}")
