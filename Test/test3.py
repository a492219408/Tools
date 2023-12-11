import ctypes
import sys
import platform
import time

import pyautogui


def send_key():
    time.sleep(3)
    pyautogui.press("d")


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except (Exception,):
        return False


if platform.system() == 'Windows':
    if is_admin():
        # 如果用户是管理员，那么就执行你的代码
        send_key()
        pass
    else:
        # 如果用户不是管理员，那么就尝试获取管理员权限
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
else:
    # 如果不是Windows系统，那么就直接执行你的代码
    send_key()
    pass
