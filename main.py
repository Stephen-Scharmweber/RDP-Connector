"""
Windows RDP Connector - GUI Tool to launch Remote Desktop sessions quickly.  
Features:  
- JSON-based server management  
- One-click RDP connection  
- Lightweight Tkinter interface  

Keywords: windows rdp, remote desktop python, json config, mstsc automation  
"""

import json
import subprocess
from tkinter import *
from tkinter import ttk

overall_font = "Righteous"
overall_background_button = "#00008B"

root = Tk()
root.title("RDP CONNECTOR")
root.config(width=430, height=70)

OPTIONS = []
with open(r'server.json', 'r') as server_json:
    json_server = json.load(server_json)
    for x in json_server:
        OPTIONS.append(x)


combo = ttk.Combobox(root, values=OPTIONS, font=("Helvetica", 14), width=20, state="readonly")
combo.set(OPTIONS[0])  # Setzen Sie die anfänglich ausgewählte Option
combo.place(x=20, y=20)

def start_action():
    server = combo.get()
    with open(r'server.json', 'r') as server_json:
        json_server = json.load(server_json)
        if server in json_server:
            selected_server_ip = json_server[server]

    rdp_command = f"mstsc /v:{selected_server_ip}"

    # Startet die RDP-Verbindung
    subprocess.Popen(rdp_command, shell=True)

start_button = Button(root, text="RDP CONNECT", command=start_action, font=(overall_font, 10),fg="Darkblue", width=15)
start_button.place(x=270, y=20)
root.mainloop()

