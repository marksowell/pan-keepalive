# PAN Keepalive

PAN Keepalive is a Python script designed to keep a Palo Alto Networks GlobalProtect VPN connection alive by periodically reconnecting every 30 minutes. This can be useful in environments where the VPN connection might drop due to inactivity.

## Description

This script uses the `PanGPA.exe` command to reconnect the VPN at regular intervals. By doing so, it ensures that the VPN connection remains active even when there is no user activity.

## Requirements

- Python 3.x
- Windows operating system
- Palo Alto Networks GlobalProtect VPN client

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/marksowell/pan-keepalive.git
    cd pan-keepalive
    ```

2. Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. Open the `pan_keepalive.py` script and verify the path to `PanGPA.exe`. The default path is:
    ```python
    globalprotect_cli = r"C:\Program Files\Palo Alto Networks\GlobalProtect\PanGPA.exe"
    ```

2. Connect to your VPN using the Palo Alto Networks GlobalProtect client.  
3. Run the script:
    ```bash
    python pan_keepalive.py
    ```

The script will run indefinitely, reconnecting the VPN every 30 minutes.

## Running the Script Automatically

You can configure the script to start automatically when your system boots. Here’s how to do it using a startup shortcut:

1. Create a Shortcut:
    - Right-click on your desktop or in a folder and select `New > Shortcut`.
    - In the location field, enter the path to your Python executable followed by the path to your script, e.g.:
      
      ```bash
      "C:\Path\To\Python\python.exe" "C:\Path\To\pan-keepalive\pan_keepalive.py"
      ```
      
    - Click `Next` and give your shortcut a name (e.g., `PAN Keepalive`).

2. Move the Shortcut to the Startup Folder:
    - Press `Win + R`, type `shell:startup`, and press Enter.
    - Move the shortcut you created into the Startup folder.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
