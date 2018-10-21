#!/usr/bin/env python
# coding=utf-8

from lifxlan import LifxLAN


def main():
    print("Discovering lights...")
    lifx = LifxLAN()

    # get devices
    devices = lifx.get_lights()
    print("\nFound {} light(s):\n".format(len(devices)))
    for d in devices:
        try:
            print(d)
        except:
            pass


if __name__ == "__main__":
    main()
