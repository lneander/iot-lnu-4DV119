import machine
import os
import pycom
from network import WLAN

# Mount SD card so we can write to log
sd = machine.SD()
os.mount(sd, '/sd')

# Connect to WiFi
wlan = WLAN(mode=WLAN.STA)
wlan.connect(ssid='yyy', auth=(WLAN.WPA2, 'xxx'))
while not wlan.isconnected():
    machine.idle()
pycom.rgbled(0x000005) # When connected to WiFi show blue ligth
