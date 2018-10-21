#!/usr/bin/env python
# coding=utf-8
from time import sleep
from light_settings import find_light


def main():
    # Locate your light
    light = find_light()
    # Turn on the light
    light.set_power('on')

    # Change the brightness of the light
    brightness = 32000                  # brightness in range [0-65535]
    light.set_brightness(brightness)

    sleep(1)

    brightness = 1
    light.set_brightness(brightness)

    sleep(1)

    brightness = 65535
    duration = 1000
    light.set_brightness(brightness, duration)

    sleep(1)

    brightness = 32000
    duration = 500
    light.set_brightness(brightness, duration)


if __name__=="__main__":
    main()
