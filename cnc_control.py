import serial
import time


class CncControl:
    s = None
    G00 = "G00 x{top} y{side} z{bottom}\n"

    def output_state(self):
        self.s.write(str.encode("$$\n"))
        time.sleep(0.1)
        while self.s.in_waiting:
            print(str(self.s.readline()))
        print("End of State Read")

    def check_for_idle(self):
        idle = False
        while not idle:
            time.sleep(0.25)
            self.s.write(str.encode("?"))
            response = str(self.s.readline())
            print(response)
            idle = response.__contains__("Idle")

    def set_value(self, value):
        self.s.write(str.encode(value))
        print(str(self.s.readline()) + " (" + value.strip('\n') + ")")

    def configure_grbl_state(self):
        self.set_value("$X\n")
        self.set_value("$3=0\n")
        self.set_value("$20=0\n")
        self.set_value("$21=0\n")
        self.set_value("$22=1\n")
        self.set_value("$27=4\n")
        self.set_value("$100=53\n")
        self.set_value("$101=53\n")
        self.set_value("$102=53\n")
        self.set_value("$110=3000\n")
        self.set_value("$111=3000\n")
        self.set_value("$112=3000\n")
        self.set_value("$120=500\n")
        self.set_value("$121=500\n")
        self.set_value("$122=500\n")
        self.set_value("G90\n")

    def clean_up(self):
        self.s.close()

    def home(self):
        self.s.write(str.encode("$H\n"))
        self.check_for_idle()

    def move_to(self, top, side, bottom):
        self.s.write(self.G00.format(top=top, side=side, bottom=bottom).encode())
        self.s.readline()
        self.check_for_idle()

    def __init__(self):
        self.s = serial.Serial('/dev/ttyUSB0', 115200)
        self.s.write(str.encode("\r\n\r\n"))
        time.sleep(2)  # Wait for grbl to initialize
        while self.s.in_waiting:
            print(str(self.s.readline()))
        self.configure_grbl_state()
        self.s.reset_input_buffer()
        self.check_for_idle()
        # self.output_state()
