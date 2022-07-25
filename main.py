import keyboard
from brake_control import BrakeControl
from control_input import ControlInput


if __name__ == '__main__':
    b = BrakeControl()
    c = ControlInput(b)
    keyboard.hook(c.perform_action)
    keyboard.wait('esc')
    b.shut_down()
