import keyboard
from brake_control import BrakeControl
from control_input import ControlInput
from cnc_control import CncControl
from screen import Screen


if __name__ == '__main__':
    b = BrakeControl()
    cnc = CncControl(b)
    screen = Screen(cnc)
    c = ControlInput(screen)
    keyboard.hook(c.perform_action)
    keyboard.wait('esc')
    cnc.clean_up()
    b.shut_down()

