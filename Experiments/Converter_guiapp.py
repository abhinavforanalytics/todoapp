import PySimpleGUI as pyg

label1 = pyg.Text("Enter Feet:")
input1 = pyg.Input()
label2 = pyg.Text("Enter Inches:")
input2 = pyg.Input()

button = pyg.Button("Convert")
window = pyg.Window("Converter Pro",layout=[[label1,input1],[label2,input2],[button]])

window.read()
window.close()