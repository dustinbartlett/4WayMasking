class Screen:
    cnc_control = None

    positions = {
        "top": 0,
        "bottom": 0,
        "vertical": 0
    }

    brake_status = {
        "top": False,
        "bottom": False,
        "vertical": False
    }

    def increment_mask_position(self, mask, distance):
        self.positions[mask] = self.positions[mask] + distance
        self.brake_status[mask] = True
        self.cnc_control.move_to(self.positions, self.brake_status)
        self.brake_status[mask] = False

    def __init__(self, cnc_control):
        self.cnc_control = cnc_control
