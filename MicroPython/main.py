"""
Created by: Ihor Chernyshev
Created on: Oct 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *

display.clear()
display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():
        pin13.write_digital(1)
        display.scroll("Red")
        pin13.write_digital(0)
        pin14.write_digital(1)
        display.scroll("Blue")
        pin14.write_digital(0)
        pin15.write_digital(1)
        display.scroll("Green")
        pin15.write_digital(0)
        pin13.write_digital(1)
        pin14.write_digital(1)
        display.scroll("Magenta")
        pin14.write_digital(0)
        pin15.write_digital(1)
        display.scroll("Yellow")
        pin13.write_digital(0)
        pin14.write_digital(1)
        display.scroll("Cyan")
        pin13.write_digital(1)
        display.scroll("White")
        pin13.write_digital(0)
        pin14.write_digital(0)
        pin15.write_digital(0)
        display.show(Image.HAPPY)
