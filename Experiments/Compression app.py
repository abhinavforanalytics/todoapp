import PySimpleGUI as pyg

label1 = pyg.Text("Select files to compress: ")
input_wid1 = pyg.Input()
button_wid1 = pyg.FolderBrowse("Choose")

label2 = pyg.Text("Select destination folder: ")
input_wid2 = pyg.Input()
button_wid2 = pyg.FolderBrowse("Choose")

window = pyg.Window("Compression Pro",
                    layout=[[label1, input_wid1, button_wid1],
                                               [label2, input_wid2, button_wid2]])
window.read()
window.close()