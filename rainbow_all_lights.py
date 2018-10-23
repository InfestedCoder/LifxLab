#!/usr/bin/env python
# coding=utf-8
from time import sleep
from lifxlan import BLUE, CYAN, GREEN, LifxLAN, ORANGE, PINK, PURPLE, RED, YELLOW


def main():
    # Locate your light
    lifx = LifxLAN(1)

    # Turn on the light
    lifx.set_power_all_lights(True)

    # Change the colors of the light
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]
    sleep_time_s = 0.1

    for color in colors:
        lifx.set_color_all_lights(color)
        sleep(sleep_time_s)

    lifx.set_power_all_lights(False)

if __name__=="__main__":
    main()


