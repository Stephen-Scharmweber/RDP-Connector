# RDP Connector

A lightweight GUI tool to quickly connect to predefined Remote Desktop servers.

## Features

- Dropdown list of servers from JSON configuration
- One-click RDP connection
- Simple and minimal interface
- Easy to add new servers

## Requirements

- Windows OS (uses mstsc.exe)
- Python 3.x
- Tkinter (usually included with Python)
- Access to Remote Desktop Connection (mstsc)

## Installation

1. Clone or download the repository
2. Ensure you have Python installed
3. Edit the `server.json` file with your servers

## Usage

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
