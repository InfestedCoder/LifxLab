#!/usr/bin/env python
# coding=utf-8
from time import sleep
from lifxlan import BLUE, CYAN, GREEN, ORANGE, PINK, PURPLE, RED, YELLOW
from light_settings import find_light


def main():
    # Locate your light
    light = find_light()

    # Turn on the light
    light.set_power('on')

    # Change the colors of the light
    colors = [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK]
    sleep_time_s = 0.2

    for color in colors:
        light.set_color(color)
        sleep(sleep_time_s)


if __name__=="__main__":
    main()
