import PySimpleGUI as sg
import http.server
import socketserver
from threading import Thread

from read_write import read_task, update_task


current_task = read_task()

layout = [
    [sg.Text("focus please")],
    [sg.InputText(current_task)],
    [sg.Button("Update message")],
    [sg.Button("Start server")],
    [sg.Text("server not running", key="servermessage")],
    [sg.Button("Quit")]
]

window = sg.Window("focus please", layout)

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 1337), Handler)

while True:
    event, values = window.read()

    if event == "Update message":
        new_task = values[0]
        new_task = new_task.strip()
        update_task(new_task)

    if event == "Start server":
        thread = Thread(target = httpd.serve_forever)
        thread.daemon = True  # server will stop when app quits
        thread.start()
        window['servermessage'].update("server is running")

    if event == "Quit" or event == sg.WIN_CLOSED:
        break

window.close()