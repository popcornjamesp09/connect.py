import re
import subprocess
from time import sleep

ips = []

print("Connect phone")
sleep(2)

ipaddr = subprocess.run(f'adb shell ip addr show wlan0', shell=True, capture_output=True)

regex = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', str(ipaddr))
if regex is not None:
    for match in regex:
        if match not in ips:
            ips.append(match)

myIp = ips[0]

print(f'Device ip is: {myIp}')

subprocess.run(f'adb tcpip 5555', shell=True, capture_output=True)

print("Please remove device.")

sleep(1.5)

subprocess.run(f'adb connect {myIp}:5555', shell=True, capture_output=True)

try:
    subprocess.run(f'scrcpy', shell=True, capture_output=True)
finally:
    print("Killing adb server")
    subprocess.run(f'adb kill-server', shell=True, capture_output=True)
