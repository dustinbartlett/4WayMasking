import RPi.GPIO as GPIO


class BrakeControl:

    axis_list = ["X", "Y", "Z"]

    axis_mapping = {
        "X": 11,
        "Y": 7,
        "Z": 5
    }

    def __get_relays(self, axis_list):
        return [self.axis_mapping[k.upper()] for k in axis_list]

    def brake_off(self, axis_list):
        GPIO.output(self.__get_relays(axis_list), GPIO.LOW)

    def brake_on(self, axis_list):
        GPIO.output(self.__get_relays(axis_list), GPIO.HIGH)

    @staticmethod
    def shut_down():
        GPIO.cleanup()

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.__get_relays(self.axis_list), GPIO.OUT)
        self.brake_on(self.axis_list)
