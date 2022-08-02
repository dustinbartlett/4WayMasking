class ControlInput:
    __bindings = None
    __screen = None
    __rate = 10
    __save_enabled = False

    def enable_save(self):
        self.__save_enabled = True

    def recall_save(self, key):
        if self.__save_enabled:
            self.__screen.save_position(key)
            self.__save_enabled = False
        else:
            self.__screen.recall_saved_position(key)

    def set_rate(self, rate):
        self.__rate = rate

    def mask_less(self, mask):
        self.__screen.increment_mask_position(mask, self.__rate)

    def mask_more(self, mask):
        self.__screen.increment_mask_position(mask, -abs(self.__rate))

    def perform_action(self, input_event):
        if input_event.event_type == 'up':
            if input_event.name in self.__bindings:
                call_tuple = self.__bindings[input_event.name]
                if len(call_tuple) == 2:
                    call_tuple[0](call_tuple[1])
                else:
                    call_tuple[0]()
            else:
                self.recall_save(input_event.name)

    def __init__(self, screen):
        self.__screen = screen
        self.__bindings = {
            "up": (self.mask_less, "top"),
            "down": (self.mask_more, "top"),
            "left": (self.mask_less, "vertical"),
            "right": (self.mask_more, "vertical"),
            "page up": (self.mask_less, "bottom"),
            "page down": (self.mask_more, "bottom"),
            "1": (self.set_rate, 0.25),
            "2": (self.set_rate, 1),
            "3": (self.set_rate, 10),
            "4": (self.set_rate, 40),
            "r": (self.enable_save,),
        }
