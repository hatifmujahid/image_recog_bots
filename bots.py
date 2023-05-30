from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con



# Point(x=415, y=644)
# Point(x=467, y=642)
# Point(x=546, y=642)
# Point(x=623, y=642)
# while True:
#     print(pyautogui.position())
#     sleep(3)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q')==False:
    if pyautogui.pixel(x=415, y=430)[0] == 0:
        click(415,430)
    elif pyautogui.pixel(x=467, y=430)[0] == 0:
        click(467,430)
    elif pyautogui.pixel(x=546, y=430)[0] == 0:
        click(546,430)
    elif pyautogui.pixel(x=623, y=430)[0] == 0:
        click(623,430)

