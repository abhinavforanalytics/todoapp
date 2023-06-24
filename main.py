##Custom function
def get_todos(filepath):
    '''
    Reading the file todos
    :rtype: object
    Todos in list format
    '''
    with open(filepath, 'r') as file :
        todos_local = file.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    '''
    :param filepath: file path where the todos are located
    :param todos_arg: todos that need to be written back
    :return: None
    '''
    with open(filepath, 'w') as file :
        file.writelines(todos_arg) ##Since we're writing,
        # it doesn't need to return anything, there's nothing to capture


while True:
    user_action = input("Type Add, Show, Edit, Complete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        task = user_action[4:] #input like 'add go to gym - 'go to gym' gets added

        todos = get_todos(filepath="Files/todo.txt")

        #appending the read input to the variable
        todos.append(task.capitalize() + '\n')
        #writing it back to the file
        write_todos(filepath="Files/todo.txt",todos_arg=todos)

    elif user_action.startswith('show') :
        #opening the file in readmode
        todos = get_todos(filepath="Files/todo.txt")
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

            todos = get_todos(filepath="Files/todo.txt")

            if number > len(todos) or number<=0:
                print(f"Please Enter valid input from 1 to {len(todos)}")
            else:
                user_edit_ = input("Enter the new todo: ")
                todos[number] = user_edit_+"\n"
                write_todos(filepath="Files/todo.txt", todos_arg=todos)
                print(f"Done!, Updated the info to '{user_edit_}'")
        except ValueError:
            print("Your command is not valid.")
            #give user the opportunity to enter the command again
            continue
#Complete
    elif user_action.startswith('complete'):
        try:
            todos = get_todos(filepath="Files/todo.txt")
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
                write_todos(filepath="Files/todo.txt",todos_arg=todos)
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

todos = get_todos(filepath="Files/todo.txt")

if len(todos) == 0:
    print(f"The list is blank")
else:
    print(f"List with {len(todos)} item(s): {str.join(',' , list(i for i in todos))}")
