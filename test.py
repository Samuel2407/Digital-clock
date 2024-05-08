"""This module holds functions to test the functionality of this project
    """
    
from digital_clock import DigitalClock
from utime import sleep

def clock_test() -> None:
    clock = DigitalClock()
    while True:
        sleep(1)
        pass
        