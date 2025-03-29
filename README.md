# RDP Connector / RDP Verbindungsmanager

A lightweight GUI tool to quickly connect to predefined Remote Desktop servers.  
Ein leichtes GUI-Tool für schnelle Verbindungen zu vordefinierten Remote Desktop Servern.

## Features / Funktionen

- Dropdown list of servers from JSON configuration / Serverauswahl per JSON-Konfiguration
- One-click RDP connection / Ein-Klick RDP-Verbindung
- Simple and minimal interface / Einfache und minimale Oberfläche
- Easy to add new servers / Einfache Serververwaltung

## Requirements / Voraussetzungen

- Windows OS (uses mstsc.exe) / Windows Betriebssystem (nutzt mstsc.exe)
- Python 3.x
- Tkinter (usually included with Python) / Tkinter (meist in Python enthalten)
- Access to Remote Desktop Connection (mstsc) / Zugriff auf Remotedesktopverbindung

## Installation

1. Clone or download the repository / Repository klonen oder herunterladen  
   ```bash
   git clone https://github.com/Stephen-Scharmweber/RDP-Connector.git
Ensure you have Python installed / Python Installation überprüfen

Edit the server.json file with your servers / server.json mit eigenen Servern bearbeiten

## Usage / Verwendung

1. Run the script: `python rdp_connector.py`
2. Select a server from the dropdown menu
3. Click "RDP CONNECT" button
4. The Remote Desktop Connection will open automatically

## Configuration

Edit `server.json` to add your servers:
```json
{
  "SERVER_DISPLAY_NAME": "IP_ADDRESS",
  "DC01": "192.168.2.10",
  "DATABASES": "192.168.2.5",
  "NEW_SERVER": "192.168.2.20"
}
