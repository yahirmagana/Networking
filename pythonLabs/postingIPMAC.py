#!/usr/bin/env python3
#
#import subprocess
#import time
#
#interface = "wlan0"
#
#myIPAddress = None
#myMACAddress = None
#
#print("Waiting for Raspberry Pi to obtain an IP address...", flush=True)
#
## Wait up to 60 seconds for an IPv4 address
#for attempt in range(12):
#    try:
#        result = subprocess.check_output(
#            ["ip", "-4", "-o", "addr", "show", "dev", interface],
#            text=True
#        )
#
#        myIPAddress = result.split()[3].split("/")[0]
#        break
#
#    except (subprocess.CalledProcessError, IndexError):
#        print("No IP address yet. Retrying in 5 seconds...", flush=True)
#        time.sleep(5)
#
## Extract MAC address
#try:
#    with open(f"/sys/class/net/{interface}/address", "r") as file:
#        myMACAddress = file.read().strip()
#except FileNotFoundError:
#    print("Could not find network interface.", flush=True)
#
#print("IP Address:", myIPAddress, flush=True)
#print("MAC Address:", myMACAddress, flush=True)
#
## Send information if IP and MAC addresses exist
#if myIPAddress and myMACAddress:
#
#    command = [
#        "curl",
#        "--fail-with-body",
#        "--show-error",
#        "--silent",
#        "--max-time", "20",
#        "--retry", "5",
#        "--retry-delay", "5",
#        "-X", "POST",
#        "https://faridfarahmand.net/EE465/checkipaddress.php",
#        "-d", f"IpAddress={myIPAddress}",
#        "-d", f"MACAddress={myMACAddress}"
#    ]
#
#    print("Sending information to server...", flush=True)
#
#    result = subprocess.run(
#        command,
#        capture_output=True,
#        text=True
#    )
#
#    print("Server response:", result.stdout, flush=True)
#
#    if result.returncode == 0:
#        print("POST request completed successfully.", flush=True)
#    else:
#        print("CURL Error:", result.stderr, flush=True)
#
#else:
#    print("No valid IP or MAC address. Request not sent.", flush=True)
#
