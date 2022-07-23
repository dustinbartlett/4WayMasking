class ControlInput:
    __bindings = []

    def top_mask_up(self):
        print("Top Mask Up")

    def top_mask_down(self):
        print("Top Mask Down")

    def perform_action(self, input_event):
        if input_event.event_type == 'up':
            self.__bindings[input_event.name]()

    def __init__(self):
        self.__bindings = {
            "up": self.top_mask_up,
            "down": self.top_mask_down,
        }
