import PySimpleGUI as PYg
from zipcreator import make_archive

label1 = PYg.Text("Select files to compress: ")
input_wid1 = PYg.Input()
button_wid1 = PYg.FilesBrowse("Choose", key="files")

label2 = PYg.Text("Select destination folder: ")
input_wid2 = PYg.Input()
button_wid2 = PYg.FolderBrowse("Choose", key='folder')

compress_button = PYg.Button("Compress")
output_label = PYg.Text(key="output_message")

window = PYg.Window("Compression Pro",
                    layout=[[label1, input_wid1, button_wid1],
                            [label2, input_wid2, button_wid2], [compress_button, output_label]])

while True:
    event, values = window.read()
    print("event: ", event, "values: ", values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output_message"].update(value="Compression Completed!")

window.close()
