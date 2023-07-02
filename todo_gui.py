import functions
import PySimpleGUI as PYg

label = PYg.Text("Enter a new todo: ")
input_box = PYg.InputText(tooltip="Enter todo", font='Community', key='todo')
add_button = PYg.Button("Add")
list_box = PYg.Listbox(values=functions.get_todos(), key='todos_list',
                       enable_events=True, size=(45, 10))  # key needed to identify list input box
edit_button = PYg.Button("Edit")
window = PYg.Window('Welcome to ToDo pro!',
                    layout=[[label], [input_box, add_button],[list_box,edit_button]],
                    font=('Community', 14))  # layout expects a list that expects list of object instances

# Edit button coded

# edit_text = PYg.InputText(tooltip="Enter todo", font='Community', key='edit_todo')
# edit_ok = PYg.Button("OK")
# edit_window = PYg.Window('Edit the Todo to:', layout=[[edit_text] ,[edit_ok]])

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    # print(3, values['todos_list'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos_list'][0]  # Dictionary -> List -> Item
            new_todo = values['todo']  # using the input text box as edited text

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)

            # edit_event, edit_value = edit_window.read()
            # new_todo = edit_value['edit_todo']
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos_list'].update(values=todos)
        case "todos_list":
            window['todo'].update(value=values['todos_list'][0])
        case PYg.WIN_CLOSED:
            break

window.close()
