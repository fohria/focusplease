import PySimpleGUI as sg
import http.server
import socketserver
from threading import Thread

layout = [
    [sg.Text("focus please")],
    [sg.InputText("this will be the focus message")],
    [sg.Button("Start server")],
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
        print("started server on 1337")

    if event == "Quit" or event == sg.WIN_CLOSED:
        break

window.close()