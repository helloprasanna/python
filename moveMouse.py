import pyautogui
import time


print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        pyautogui.moveTo(x+5, y+5)
        print('X : {}, Y : {} '.format(x, y))

        time.sleep(5)
except KeyboardInterrupt:
    print('Terminated \n')
