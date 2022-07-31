import RPi.GPIO as GPIO
import time


class BrakeControl:

    relay1 = 11
    relay2 = 7
    relay3 = 5
    relays = [relay1, relay2, relay3]

    def brake_off(self):
        GPIO.output(self.relays, GPIO.LOW)

    def brake_on(self):
        GPIO.output(self.relays, GPIO.HIGH)

    @staticmethod
    def shut_down():
        GPIO.cleanup()

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relays, GPIO.OUT)
        self.brake_on()
