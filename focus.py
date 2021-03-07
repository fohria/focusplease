import PySimpleGUI as sg
import http.server
import socketserver
from threading import Thread

from read_write import read_content, read_task, find_task_lineindex, update_task

layout = [
    [sg.Text("focus please")],
    [sg.InputText("this will be the focus message")],
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

    if event == "Start server":
        thread = Thread(target = httpd.serve_forever)
        thread.daemon = True  # server will stop when app quits
        thread.start()
        window['servermessage'].update("server is running")

    if event == "Quit" or event == sg.WIN_CLOSED:
        break

window.close()