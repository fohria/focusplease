import PySimpleGUI as sg

layout = [
    [sg.Text("focus please")],
    [sg.InputText("this will be the focus message")],
    [sg.Button("Start server")],
    [sg.Button("Stop server")],
    [sg.Button("Quit")]
]

window = sg.Window("focus please", layout)

while True:
    event, values = window.read()

    if event == "Quit" or event == sg.WIN_CLOSED:
        break

window.close()