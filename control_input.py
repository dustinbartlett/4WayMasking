from brake_control import BrakeControl

class ControlInput:
    __bindings = []
    brake_control = None

    def top_mask_up(self):
        print("Brake On")
        self.brake_control.brake_on()

    def top_mask_down(self):
        print("Brake Off")
        self.brake_control.brake_off()

    def perform_action(self, input_event):
        if input_event.event_type == 'up':
            self.__bindings[input_event.name]()

    def __init__(self, brake_control):
        self.brake_control = brake_control
        self.__bindings = {
            "up": self.top_mask_up,
            "down": self.top_mask_down,
        }
