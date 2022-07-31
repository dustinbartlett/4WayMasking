class ControlInput:
    __bindings = None
    screen = None

    def top_mask_up(self):
        self.screen.increment_mask_position("top", 30)

    def top_mask_down(self):
        self.screen.increment_mask_position("top", -30)

    def bottom_mask_up(self):
        self.screen.increment_mask_position("bottom", 30)

    def bottom_mask_down(self):
        self.screen.increment_mask_position("bottom", -30)

    def vertical_masks_in(self):
        self.screen.increment_mask_position("vertical", 30)

    def vertical_masks_out(self):
        self.screen.increment_mask_position("vertical", -30)

    def perform_action(self, input_event):
        if input_event.event_type == 'up':
            self.__bindings[input_event.name]()

    def __init__(self, screen):
        self.screen = screen
        self.__bindings = {
            "up": self.top_mask_up,
            "down": self.top_mask_down,
            "left": self.vertical_masks_in,
            "right": self.vertical_masks_out,
            "page up": self.bottom_mask_up,
            "page down": self.bottom_mask_down
        }
