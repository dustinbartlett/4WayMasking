class ControlInput:
    __bindings = None
    __screen = None
    __rate = 30
    __save_enabled = False

    def enable_save(self):
        self.__save_enabled = True

    def recall_save(self, key):
        if self.__save_enabled:
            self.__screen.save_position(key)
            self.__save_enabled = False
        else:
            self.__screen.recall_saved_position(key)

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
            if input_event.name in self.__bindings:
                self.__bindings[input_event.name]()
            else:
                self.recall_save(input_event.name)

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
            "r": self.enable_save,
        }
