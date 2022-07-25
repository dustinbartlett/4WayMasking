import RPi.GPIO as GPIO


class BrakeControl:

    relay1 = 11
    relay2 = 7
    relay3 = 5

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.relay1, GPIO.OUT)
        GPIO.setup(self.relay2, GPIO.OUT)
        GPIO.setup(self.relay3, GPIO.OUT)

    def brake_off(self):
        GPIO.output(self.relay1, GPIO.HIGH)
        GPIO.output(self.relay2, GPIO.HIGH)
        GPIO.output(self.relay3, GPIO.HIGH)

    def brake_on(self):
        GPIO.output(self.relay1, GPIO.LOW)
        GPIO.output(self.relay2, GPIO.LOW)
        GPIO.output(self.relay3, GPIO.LOW)

    def shut_down(self):
        GPIO.cleanup()