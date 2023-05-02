import PySimpleGUI as Sg
from Functions import read, add, delete


def show():
    refreshed_to_do_list = read()
    window['-LIST-'].update(values=refreshed_to_do_list)


to_do_list = read()

button_Show = Sg.Button("Select")
button_Add = Sg.Button("Add")
textBox_Add = Sg.InputText(tooltip='enter new to do'.title(), key='-Add-')
button_Delete = Sg.Button("Delete")
list_box = Sg.Listbox(values=to_do_list, size=(20, 10), key='-LIST-')

window = Sg.Window("to do app".title(),
                   layout=[[button_Show],
                           [button_Add, textBox_Add],
                           [button_Delete],
                           [list_box]], font=('Times New Roman', 20))

while True:
    event, value = window.read()
    print(event, value)
    if event == 'Select':
        window['-Add-'].update(value=value['-LIST-'][0])
    elif event == 'Add':
        to_do_new = value['-Add-']
        print(to_do_new)
        if to_do_new != '':
            add(to_do_new)
            show()
            window['-Add-'].update(value='')
        else:
            Sg.Popup('please type a to do to add it'.title())
    elif event == 'Delete':
        try:
            to_do_to_delete = value['-LIST-'][0]
            print(to_do_to_delete)
            delete(to_do_to_delete)
            show()
        except IndexError:
            Sg.Popup('please select a to do to delete'.title())
    else:
        exit()
