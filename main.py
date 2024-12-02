import os
import sys
import subprocess

def checkNetwork():
    # Use nmcli for Linux
    iNet = []
    try:
        result = subprocess.run(
            ["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"],
            capture_output=True, text=True
        )
        active_networks = [
            line.split(":")[1]
            for line in result.stdout.splitlines()
            if line.startswith("yes")
        ]
        iNet.append(active_networks[0] if active_networks else None)

        return iNet
    except Exception as e:
        print(f"Error checking Wi-Fi: {e}")
        return None

def printValues(aNet:list) -> bool:
    try:
        for value in aNet:
            print(value)
    
        return True
    except Exception as e:
        return False

if __name__ == "__main__":
    try:
        iNet = checkNetwork()
        prnt = printValues(iNet)
        if prnt:
            sys.exit("\n")
        else:
            print("Could not print values")
            sys.exit("\n")
        sys.exit()
    except KeyboardInterrupt:
        sys.exit("\n")
