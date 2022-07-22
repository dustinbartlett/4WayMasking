from global_hotkeys import *


class ControlInput:
    __exit_call_received = False

    def top_mask_up(self):
        print("Top Mask Up")

    def top_mask_down(self):
        print("Top Mask Down")

    def exit_application(self):
        print("Exiting")
        stop_checking_hotkeys()
        self.__exit_call_received = True

    def exit_call_received(self):
        return self.__exit_call_received

    def __init__(self):
        bindings = [
            [["up"], None, self.top_mask_up],
            [["down"], None, self.top_mask_down],
            [["control", "x"], None, self.exit_application],
        ]

        register_hotkeys(bindings)
        start_checking_hotkeys()
