import pyautogui
import pyautogui as pg
from time import sleep

sleep(3)

print(pyautogui.locateOnScreen("yes.png"))

# inputValue 575 336
# double 890 400
# submitBtn 1400 530

realBetAfter = 5
realBetStart = 600
loseStreak = 0
betCounter = 0


while True:
    if betCounter > 1000:
        betCounter = 0
        pyautogui.keyDown('f5')
        pyautogui.keyUp('f5')
        sleep(10)
    if loseStreak < realBetAfter:
        pyautogui.doubleClick(x=574, y=336)
        pyautogui.typewrite('20')
        sleep(0.1)
        pyautogui.click(x=1400, y=530)
        sleep(0.5)
        no = pyautogui.locateOnScreen('./no.png')
        yes = pyautogui.locateOnScreen('yes.png')
        if no != None:
            loseStreak += 1
        if yes != None:
            loseStreak = 0
        betCounter += 1
        sleep(0.1)
        continue
    pyautogui.doubleClick(x=574, y=336)
    pyautogui.typewrite(str(realBetStart))
    sleep(0.2)
    pyautogui.click(x=1400, y=530)
    sleep(0.6)
    yes = pyautogui.locateOnScreen('yes.png')
    no = pyautogui.locateOnScreen('no.png')
    if yes != None:
        loseStreak = 0
        betCounter += 1
        continue
    while True:
        pyautogui.click(x = 890, y = 400)
        sleep(0.1)
        pyautogui.click(x=1400, y=530)
        sleep(0.6)
        yes = pyautogui.locateOnScreen('yes.png')
        if yes != None:
            loseStreak = 0
            betCounter += 1
            break



