import PySimpleGUI as Sg
import Functions_Conversion

label_foot = Sg.Text("enter foot: ".title())
label_inches = Sg.Text("enter inches: ".title())
label_meter = Sg.Text(key='_meter_')

textbox_foot = Sg.InputText(key='_foot_')
textbox_inches = Sg.InputText(key='_inches_')

button_convert = Sg.Button("Convert")
button_exit = Sg.Button("Exit")

window = Sg.Window("Conversion",
                   layout=[[label_foot, textbox_foot],
                           [label_inches, textbox_inches],
                           [button_convert, label_meter],
                           [button_exit]])

while True:
    event, value = window.read()
    print(event, value)
    print(value['_foot_'])
    if event == 'Exit':
        break
    try:
        foot = float(value['_foot_'])
        inches = float(value['_inches_'])
        meter = Functions_Conversion.ft_to_meter(foot, inches)

        if event == 'Convert':
            window['_meter_'].update(value=f'{meter} meters')

    except ValueError:
        Sg.Popup('please fill the empty text boxes by numbers!'.title())
