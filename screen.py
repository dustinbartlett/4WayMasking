import copy
import json


class Screen:
    cnc_control = None

    __positions = {
        "top": 0,
        "bottom": 0,
        "vertical": 0
    }

    __brake_status = {
        "top": "off",
        "bottom": "off",
        "vertical": "off"
    }

    __saved_positions = {}

    def __reset_brake_status(self):
        for key in self.__brake_status.keys():
            self.__brake_status[key] = "off"

    def __all_on_brake_status(self):
        for key in self.__brake_status.keys():
            self.__brake_status[key] = "on"

    def increment_mask_position(self, mask, distance):
        self.__positions[mask] = self.__positions[mask] + distance
        self.__brake_status[mask] = "on"
        self.cnc_control.move_to(self.__positions, self.__brake_status)
        self.__reset_brake_status()

    def save_position(self, key):
        self.__saved_positions[key] = copy.deepcopy(self.__positions)
        json.dump(self.__saved_positions, open("saved_mask_positions.json", 'w'))

    def recall_saved_position(self, key):
        self.__all_on_brake_status()
        self.__positions = copy.deepcopy(self.__saved_positions[key])
        self.cnc_control.move_to(self.__positions, self.__brake_status)
        self.__reset_brake_status()

    def __init__(self, cnc_control):
        self.cnc_control = cnc_control
        self.__saved_positions = json.load(open("saved_mask_positions.json"))
