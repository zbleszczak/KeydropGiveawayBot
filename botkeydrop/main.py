from time import sleep
from datetime import datetime
import pyautogui
import atexit

giveawaycounter = 0
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


while True:
    try:
        pos = pyautogui.locateOnScreen('dolacz.png')
        if pos != None:
            print("Ostatnia data dolaczenia do giveaway'u: ")
            print("Ostatnie dolaczenie do giveaway'a - " + datetime.now().strftime("%H:%M:%S"))
            sleep(5)
            pyautogui.keyDown("f5")
            pyautogui.keyUp("f5")
            sleep(7)
            pyautogui.click(pos[0], pos[1])
            sleep(5)
            pyautogui.click(589, 823)
            sleep(6)
            pyautogui.click(783, 50)
            sleep(2)
            pyautogui.keyDown("backspace")
            pyautogui.keyUp("backspace")
            sleep(2)
            pyautogui.keyDown("ctrl")
            pyautogui.keyDown("v")
            pyautogui.keyUp("ctrl")
            pyautogui.keyUp("v")
            pyautogui.keyDown("enter")
            pyautogui.keyUp("enter")
    except:
        print("Nie znaleziono obrazu dolaczenia do giveawayu")
