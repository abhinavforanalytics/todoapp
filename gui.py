import functions
import PySimpleGUI as pyg

label = pyg.Text("Enter a new todo: ")
input_box = pyg.InputText(tooltip="Enter todo: ")
add_button = pyg.Button("Add")

window = pyg.Window('Welcome to ToDo pro!',layout = [[label],[input_box],[add_button]]) #layout expects a list that expects list of object instances
window.read()
window.close()