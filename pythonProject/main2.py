import pyautogui
import time
import keyboard

# 878, 565 to 912, 611

def farm(dire):
    if dire == 0:
        pyautogui.keyDown('a')
        pyautogui.keyDown("w")
        time.sleep(96)
        pyautogui.keyUp('a')
        pyautogui.keyUp("w")

    else:
        pyautogui.keyDown('d')
        pyautogui.keyDown("w")
        time.sleep(96)
        pyautogui.keyUp('d')
        pyautogui.keyUp("w")





time.sleep(2)

while True:
    farm(0)
    print("done")
    pyautogui.keyDown("s")
    time.sleep(.5)
    pyautogui.keyUp("s")
    farm(1)
    time.sleep(.1)
    farm(0)
    pyautogui.keyDown("s")
    time.sleep(.5)
    pyautogui.keyUp("s")
    farm(1)
    time.sleep(.1)
    farm(0)
    pyautogui.keyDown("s")
    time.sleep(.5)
    pyautogui.keyUp("s")
    farm(1)
    time.sleep(.5)
    pyautogui.press("n")
    time.sleep(1)
