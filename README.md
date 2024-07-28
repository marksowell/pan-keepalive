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
    git clone https://github.com/yourusername/pan-keepalive.git
    cd pan-keepalive
    ```

2. Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## Usage

1. Open the `pan_keepalive.py` script and verify the path to `PanGPA.exe`. The default path is:
    ```python
    globalprotect_cli = r"C:\Program Files\Palo Alto Networks\GlobalProtect\PanGPA.exe"
    ```

2. Run the script:
    ```bash
    python pan_keepalive.py
    ```

The script will run indefinitely, reconnecting the VPN every 30 minutes.

## Running the Script Automatically

To run the script automatically in the background, you can use Windows Task Scheduler:

1. Open Task Scheduler (press `Win + R`, type `taskschd.msc`, and press Enter).

2. Create a new basic task:
    - Name: Keep VPN Alive
    - Trigger: Daily (set the start time and frequency as needed)
    - Action: Start a program
    - Program/script: Path to your Python executable, e.g., `C:\Path\To\Python\python.exe`
    - Add arguments: Path to your script file, e.g., `C:\Path\To\pan-keepalive\pan_keepalive.py`

3. Finish and save the task.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
