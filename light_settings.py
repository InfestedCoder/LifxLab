#!/usr/bin/env python
# coding=utf-8
from lifxlan import Light

# Put the mac and ip address of your light here
# You can find both values by running find_all_lights.py
MAC_ADDRESS = "d0:73:d5:34:66:8f"
IP_ADDRESS = "192.168.1.131"


def find_light():
    # Locate your light by name
    light = Light(MAC_ADDRESS, IP_ADDRESS)

    # If light is not found, print a message and exit
    if light is None:
        print("Unable to find light, make sure settings are correct in light_settings.py, the light is plugged in, and "
              "the laptop is connected to the DPS Career Day network")

    return light
