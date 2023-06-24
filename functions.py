##Custom function
def get_todos(filepath="Files/todo.txt") :
    '''
    Reading the file todos
    :rtype: object
    Todos in list format
    '''
    with open(filepath, 'r') as file :
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg,
                filepath="Files/todo.txt") :  # non-default parameter should always be before default parameter
    '''
    :param filepath: file path where the todos are located
    :param todos_arg: todos that need to be written back
    :return: None
    '''
    with open(filepath, 'w') as file :
        file.writelines(todos_arg)  ##Since we're writing,
        # it doesn't need to return anything, there's nothing to capture
