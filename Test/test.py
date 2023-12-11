import random
import time
import pyautogui
from pynput import keyboard

# totalMin = 20
totalSec = 10
if "totalMin" in vars():
    totalTime = totalMin * 60
else:
    totalTime = totalSec


# while totalTime > 0:
#     random_number = random.randint(1, 3)
#     totalTime = totalTime - random_number
#     print(1)
#     time.sleep(random_number)
# pyautogui.press("e")


def on_activate_h():
    global totalTime
    while totalTime > 0:
        random_number = random.randint(1, 3)
        totalTime = totalTime - random_number
        print(1)
        time.sleep(random_number)


def on_activate_i():
    print('<alt>+w pressed')


with keyboard.GlobalHotKeys({'<alt>+e': on_activate_h, '<alt>+w': on_activate_i}) as h:
    h.join()
