from math import fabs
import os
import pyautogui
import time


def wp():
    os.system("open /Applications/Whatsapp.app")
    time.sleep(10)
    # pyautogui.click(941,457, clicks =2); pyautogui.typewrite('Hello world \n')
    # pyautogui.screenshot('tab1.png',region=(0,0,1697,153))
    x,y= pyautogui.locateCenterOnScreen('screen.png', confidence=0.5)
    pyautogui.click(x/2,y/2)
    pyautogui.typewrite('MASOOD AHAMED\n')
    print(x,y)


    sendx,sendy= pyautogui.locateCenterOnScreen('send_msg.png', confidence=0.5)
    pyautogui.click(sendx/2,sendy/2)
    pyautogui.typewrite('This is test message\n')


wp()
