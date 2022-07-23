import keyboard
from control_input import ControlInput


if __name__ == '__main__':
    c = ControlInput()
    keyboard.hook(c.perform_action)
    keyboard.wait('esc')
