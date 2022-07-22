import time
from control_input import ControlInput

if __name__ == '__main__':
    c = ControlInput()
    while not c.exit_call_received():
        time.sleep(0.1)
