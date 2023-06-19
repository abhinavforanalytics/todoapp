##Custom function
def get_todos():
    with open("Files/todo.txt", 'r') as file :
        todos = file.readlines()
    return todos


while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        task = user_action[4:] #input like 'add go to gym - 'go to gym' gets added

        todos = get_todos()

        #appending the read input to the variable
        todos.append(task.capitalize() + '\n')
        #writing it back to the file
        with open("Files/todo.txt",'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show') :
        #opening the file in readmode
        todos = get_todos()
        #check if there are any tasks in the list
        if todos:
            print(f"Your pending tasks are: ")
            # eliminating the "\n" from the end of the list
            newtasks = [item.strip("\n") for item in todos]
            for index, item in enumerate(newtasks):
                print(f"{index + 1}-{item.strip()}")
        else:
            print("You have no pending tasks!")
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number-1

            todos = get_todos()

            if number > len(todos) or number<=0:
                print(f"Please Enter valid input from 1 to {len(todos)}")
            else:
                user_edit_ = input("Enter the new todo: ")
                todos[number] = user_edit_+"\n"
                with open("Files/todo.txt", 'w') as file:
                    file.writelines(todos)
                print(f"Done!, Updated the info to '{user_edit_}'")
        except ValueError:
            print("Your command is not valid.")
            #give user the opportunity to enter the command again
            continue
#Complete
    elif user_action.startswith('complete'):
        try:
            todos = get_todos()
            #check if there are any tasks in the list
            if todos:
                print(f"Your pending tasks are: ")
                # eliminating the "\n" from the end of the list
                todos = [item.strip("\n") for item in todos]
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
        except IndexError:
            print("Please enter number values within the list index.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid, please keep the inputs as stated above")

todos = get_todos()

if len(todos) == 0:
    print(f"The list is blank")
else:
    print(f"List with {len(todos)} item(s): {str.join(',' , list(i for i in todos))}")
