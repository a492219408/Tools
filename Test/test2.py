import copy
import random
from threading import Thread
import time
import pyautogui

key_interval_delay = 0.1
totalTime = 30
# timeType = "min"


def send_key(key, key_type=""):
    if key_type == "" or key_type.lower() == "p" or key_type.lower() == "press":
        pyautogui.press(key)
        time.sleep(key_interval_delay)
    elif key_type.lower() == "d" or key_type.lower() == "down":
        pyautogui.keyDown(key)
        time.sleep(key_interval_delay)
    elif key_type.lower() == "u" or key_type.lower() == "up":
        pyautogui.keyUp(key)
        time.sleep(key_interval_delay)


def skill_up():
    total_time_deepcopy = copy.deepcopy(totalTime)
    while total_time_deepcopy > 0:
        time.sleep(random.randint(30, 35))
        send_key("ctrl", "d")
        send_key("r")
        send_key("w")
        send_key("e")
        send_key("q")
        send_key("ctrl", "u")


def you_mi_skill_w():
    total_time_deepcopy = copy.deepcopy(totalTime)
    while total_time_deepcopy > 0:
        time.sleep(random.randint(20, 60))
        f_key = str(random.randint(1, 5))
        pyautogui.moveTo(1965, 1017)
        send_key("f" + f_key, "d")
        send_key("w")
        send_key("f" + f_key, "u")


def you_mi_skill():
    total_time_deepcopy = copy.deepcopy(totalTime)
    while total_time_deepcopy > 0:
        time.sleep(random.randint(20, 25))
        send_key("e")
        send_key("r")
        send_key("d")


threads = [Thread(target=skill_up), Thread(target=you_mi_skill_w), Thread(target=you_mi_skill)]

if __name__ == '__main__':
    time.sleep(3)
    pyautogui.press("d")
    # for thread in threads:
    #     thread.start()
