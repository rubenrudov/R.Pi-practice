import os
import RPi.GPIO as GPIO
from time import sleep


def ping():
    """
    :return: if the ping to google succeeded RED, else: BLUE
    """
    hostname = "google.com"
    response = os.system("ping -c 1 " + hostname)

    if response == 0:
        color = "RED"  # If was able to ping google, color is red

    else:
        color = "BLUE"  # If wasn't able to ping google, color is blue and won't be shown

    return color


def main():
    color = ping()
    while True:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH)

        if color is "RED":
            sleep(1)
            GPIO.output(8, GPIO.LOW)
            sleep(1)
            GPIO.output(8, GPIO.HIGH)

        # TODO: Add blue light lighting if no connection to google (Not possible for remote running)

        print("Looped %s", color)   # Aware yourself that one loop has happened


if __name__ == '__main__':
    main()
