import pyautogui
import time
import keyboard

# 878, 565 to 912, 611

def farm(dire):
    if dire == 0:
        pyautogui.keyDown('d')
        pyautogui.mouseDown()
        time.sleep(72)
        pyautogui.keyUp('d')
        pyautogui.mouseUp()

    else:
        pyautogui.keyDown('a')
        pyautogui.mouseDown()
        time.sleep(72)
        pyautogui.keyUp('a')
        pyautogui.mouseUp()


def det():
    pic = pyautogui.screenshot(region=(908, 574, 32, 41))
    width, height = pic.size

    for x in range(0, width, 7):
        for y in range(0, height, 7):
            r,g,b = pic.getpixel((x,y))

            if r==255:
                pyautogui.press('m')
                time.sleep(3)
                pyautogui.press('n')
                time.sleep(3)
                for i in range(2):
                    pyautogui.keyDown('space')
                    time.sleep(.05)
                    pyautogui.keyUp('space')


time.sleep(2)
counter = 0
while True:
    count = 0
    if counter==8:
        pyautogui.press('m')
        time.sleep(60)
        pyautogui.press('n')
        time.sleep(3)
        #for i in range(2):
            #pyautogui.keyDown('space')
            #time.sleep(.05)
            #pyautogui.keyUp('space')
        counter = 0
    for i in range(8):
        for i in range(3):
            farm(count)
            if count == 0:
                count = 1
            else:
                count = 0

        pyautogui.keyDown('w')
        time.sleep(1.1)
        pyautogui.keyUp('w')
    pyautogui.press('n')
    counter+=1
