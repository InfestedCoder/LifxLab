#!/usr/bin/env python
# coding=utf-8
from time import sleep
from light_settings import find_light


def main():
    # Locate your light
    light = find_light()

    # Turn on the light
    light.set_power('on')

    # Pause for 1 second
    sleep(1)

    # Turn off the light
    light.set_power('off')


if __name__=="__main__":
    main()
