import PySimpleGUI

label_height = PySimpleGUI.Text("Your Height: ")
label_weight = PySimpleGUI.Text("Your Weight: ")
inputBox_height = PySimpleGUI.InputText(tooltip="Height")
inputBox_weight = PySimpleGUI.InputText(tooltip="Weight")
button_OK = PySimpleGUI.Button("OK")

window = PySimpleGUI.Window("BMI Calculator",
                            layout=[[label_height, inputBox_height],
                                    [label_weight, inputBox_weight],
                                    [button_OK]])

window.read()
window.close()

