#!/usr/bin/env python
# coding=utf-8
from lifxlan import BLUE, CYAN, GREEN, ORANGE, PINK, PURPLE, RED, YELLOW
from light_settings import find_light


def main():
    # Locate your light
    light = find_light()

    # Turn on the light
    light.set_power('on')

    # Change the color of the light
    light.set_color(BLUE)


if __name__=="__main__":
    main()
