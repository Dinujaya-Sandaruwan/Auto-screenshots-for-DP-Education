import pyautogui
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
taken = True
# print(taken)

# print(res)

while True:
    res = pyautogui.locateOnScreen("image.png")
    if res != None:
        # print(taken)
        if taken == True:
            print("Screenshot Taken")

            # Press and release -> Win + Print_Screen
            keyboard.press(Key.cmd)
            keyboard.press(Key.print_screen)
            keyboard.release(Key.print_screen)
            keyboard.release(Key.cmd)

            taken = False
            # print(taken)

            # time.sleep(3)
    else:
        taken = True
        # print(taken)
    # time.sleep(0.100)
