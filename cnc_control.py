import serial
import time


class CncControl:
    serial_port = None
    G00 = "G00 x{top} y{vertical} z{bottom}\n"
    brake_control = None
    axis_mapping = {
        "top": "X",
        "vertical": "Y",
        "bottom": "Z"
    }

    def __check_for_idle(self):
        idle = False
        while not idle:
            time.sleep(0.25)
            self.serial_port.write(str.encode("?"))
            response = str(self.serial_port.readline())
            # print(response)
            idle = response.__contains__("Idle")

    def __set_value(self, value):
        self.serial_port.write(str.encode(value))
        self.serial_port.readline()
        # print(str(self.serial_port.readline()) + " (" + value.strip('\n') + ")")

    def __configure_grbl_state(self):
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200)
        self.serial_port.write(str.encode("\r\n\r\n"))
        time.sleep(2)  # Wait for grbl to initialize
        while self.serial_port.in_waiting:
            self.serial_port.readline()
            # print(str(self.serial_port.readline()))
        self.__set_value("$X\n")
        self.__set_value("$3=0\n")
        self.__set_value("$20=0\n")
        self.__set_value("$21=0\n")
        self.__set_value("$22=1\n")
        self.__set_value("$27=4\n")
        self.__set_value("$100=53\n")
        self.__set_value("$101=53\n")
        self.__set_value("$102=53\n")
        self.__set_value("$110=3000\n")
        self.__set_value("$111=3000\n")
        self.__set_value("$112=3000\n")
        self.__set_value("$120=500\n")
        self.__set_value("$121=500\n")
        self.__set_value("$122=500\n")
        self.__set_value("G90\n")

    def __get_axis_list(self, brake_status):
        return [self.axis_mapping[k.lower()] for k in brake_status if brake_status[k].lower() == "on"]

    def __send_gcode(self, gcode, brake_axis_list):
        self.brake_control.brake_off(brake_axis_list)
        time.sleep(0.2)
        self.serial_port.write(str.encode(gcode))
        self.serial_port.readline()
        self.__check_for_idle()
        time.sleep(0.2)
        self.brake_control.brake_on(brake_axis_list)

    def output_state(self):
        self.serial_port.write(str.encode("$$\n"))
        time.sleep(0.1)
        while self.serial_port.in_waiting:
            print(str(self.serial_port.readline()))
        print("End of State Read")

    def clean_up(self):
        self.serial_port.close()
        self.brake_control.shut_down()

    def home(self):
        self.__send_gcode("$H\n", self.brake_control.axis_list)

    def move_to(self, positions, brake_status):
        self.__send_gcode(self.G00.format(top=positions["top"],
                                          vertical=positions["vertical"],
                                          bottom=positions["bottom"]),
                          self.__get_axis_list(brake_status))

    def __init__(self, brake_control):
        self.brake_control = brake_control
        self.__configure_grbl_state()
        self.serial_port.reset_input_buffer()
        self.__check_for_idle()
        # self.output_state()
