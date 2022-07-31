class ControlInput:
    __bindings = None
    __screen = None
    __rate = 30

    def set_rate_fine(self):
        self.__rate = 1

    def set_rate_small(self):
        self.__rate = 5

    def set_rate_coarse(self):
        self.__rate = 30

    def top_mask_up(self):
        self.__screen.increment_mask_position("top", self.__rate)

    def top_mask_down(self):
        self.__screen.increment_mask_position("top", -abs(self.__rate))

    def bottom_mask_up(self):
        self.__screen.increment_mask_position("bottom", self.__rate)

    def bottom_mask_down(self):
        self.__screen.increment_mask_position("bottom", -abs(self.__rate))

    def vertical_masks_in(self):
        self.__screen.increment_mask_position("vertical", self.__rate)

    def vertical_masks_out(self):
        self.__screen.increment_mask_position("vertical", -abs(self.__rate))

    def perform_action(self, input_event):
        if input_event.event_type == 'up':
            print(input_event.name)
            self.__bindings[input_event.name]()

    def __init__(self, screen):
        self.__screen = screen
        self.__bindings = {
            "up": self.top_mask_up,
            "down": self.top_mask_down,
            "left": self.vertical_masks_in,
            "right": self.vertical_masks_out,
            "page up": self.bottom_mask_up,
            "page down": self.bottom_mask_down,
            "1": self.set_rate_fine,
            "2": self.set_rate_small,
            "3": self.set_rate_coarse,
        }
