#!/usr/bin/env python3
import pyfirmata
from time import sleep

# board = pyfirmata.Arduino('/dev/ttyUSB1')
serial_path = '/dev/serial/by-id/usb-1a86_USB2.0-Serial-if00-port0'
board = pyfirmata.Arduino(serial_path)


def blink():
    board.digital[13].write(1)
    sleep(1)
    board.digital[13].write(0)
    sleep(1)


def main():
    try:
        while True:
            blink()
    except KeyboardInterrupt:
        print()

if __name__ == '__main__':
    main()
