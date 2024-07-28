import os
import time
import subprocess

# Path to PanGPA.exe
globalprotect_cli = r"C:\Program Files\Palo Alto Networks\GlobalProtect\PanGPA.exe"

# Function to reconnect VPN
def reconnect_vpn():
    try:
        subprocess.run([globalprotect_cli, "-reconnect"], check=True)
        print("Reconnected VPN successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to reconnect VPN: {e}")

# Infinite loop to keep the connection alive
while True:
    print("Reconnecting VPN...")
    reconnect_vpn()
    
    # Wait for 30 minutes before the next reconnect
    time.sleep(1800)
