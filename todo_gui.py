import functions
import PySimpleGUI as pyg

label = pyg.Text("Enter a new todo: ")
input_box = pyg.InputText(tooltip="Enter todo: ", font=('Calibri'), key='todo')
add_button = pyg.Button("Add")

window = pyg.Window('Welcome to ToDo pro!',
                    layout=[[label], [input_box, add_button]],
                    font=('Community', 14))  # layout expects a list that expects list of object instances
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo']+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case pyg.WIN_CLOSED:
            break



window.close()
