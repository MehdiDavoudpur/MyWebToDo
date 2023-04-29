import PySimpleGUI

'''label_height = PySimpleGUI.Text("Your Height: ")
label_weight = PySimpleGUI.Text("Your Weight: ")
inputBox_height = PySimpleGUI.InputText(tooltip="Height")
inputBox_weight = PySimpleGUI.InputText(tooltip="Weight")'''

button_Show = PySimpleGUI.Button("Show")
button_Add = PySimpleGUI.Button("Add")
button_Delete = PySimpleGUI.Button("Delete")
button_Edit = PySimpleGUI.Button("Edit")

window = PySimpleGUI.Window("BMI Calculator",
                            layout=[[button_Show],
                                    [button_Add],
                                    [button_Delete],
                                    [button_Edit]])

window.read()
