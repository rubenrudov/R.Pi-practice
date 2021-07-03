"""
Author: Ruben Rudov
Date: 02/07/2021
Purpose: Light up and down the LED that connected through power channel and channel 8 of the R.Pi
"""
from time import sleep
import RPi.GPIO as GPIO


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)

    for i in range(10):
        GPIO.output(8, GPIO.HIGH)   # LED shut down
        sleep(1)
        GPIO.output(8, GPIO.LOW)    # LED light up
        sleep(1)
        print("looped")     # Aware yourself that one loop has happened


if __name__ == '__main__':
    main()
