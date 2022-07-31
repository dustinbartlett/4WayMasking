import time


class ControlInput:
    __bindings = []
    brake_control = None
    cnc_control = None

    def top_mask_up(self):
        self.brake_control.brake_off()
        time.sleep(0.3)
        self.cnc_control.move_to(-30, -30, -30)
        time.sleep(0.3)
        self.brake_control.brake_on()

    def top_mask_down(self):
        self.brake_control.brake_off()
        time.sleep(0.3)
        self.cnc_control.move_to(30, 30, 30)
        time.sleep(0.3)
        self.brake_control.brake_on()

    def perform_action(self, input_event):
        if input_event.event_type == 'up':
            self.__bindings[input_event.name]()

    def __init__(self, brake_control, cnc_control):
        self.brake_control = brake_control
        self.cnc_control = cnc_control
        self.__bindings = {
            "up": self.top_mask_up,
            "down": self.top_mask_down,
        }
